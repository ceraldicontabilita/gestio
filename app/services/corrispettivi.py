"""Import dei corrispettivi RT: dalla XML alla giornata canonica e alle
scritture di Prima Nota (docs/spec/03_PAGINE/LOGICA_JSON/06-corrispettivi.json).

Regola vincolante (docs/spec/01_MASTER/ISTRUZIONI_AGENTI.md): il ricavo
nasce SOLO dal corrispettivo RT. La quota contanti entra subito in Prima
Nota Cassa; la quota elettronico è un credito POS atteso, registrato in
Prima Nota Banca con stato "attesa" — l'accredito reale del gestore lo
riconcilia in un secondo momento (non è ancora costruito: vedi modulo
Coerenza POS, docs/spec/03_PAGINE/40-coerenza-pos.md).
"""

import hashlib
import uuid
from decimal import Decimal

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.models import Conto, Corrispettivo, PrimaNotaMovimento, StatoMovimento, TipoMovimento
from app.parsers.corrispettivi_rt import CorrispettivoRT, parse_corrispettivo_xml
from app.services import scritture_contabili


def _new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex}"


def importa_corrispettivo_xml(
    db: Session, *, xml_bytes: bytes, source: str = "import_manuale"
) -> Corrispettivo:
    """Importa un XML di corrispettivi RT. Idempotente per dispositivo/data:
    un secondo import dello stesso giorno restituisce la giornata già
    registrata senza duplicare né la giornata né le scritture di Prima Nota."""
    parsed: CorrispettivoRT = parse_corrispettivo_xml(xml_bytes)
    file_hash = hashlib.sha256(xml_bytes).hexdigest()

    esistente = db.scalar(
        select(Corrispettivo).where(
            Corrispettivo.id_dispositivo == parsed.id_dispositivo,
            Corrispettivo.data_rilevazione == parsed.data_ora_rilevazione.date(),
        )
    )
    if esistente is not None:
        return esistente

    operation_id = _new_id("op")
    corrispettivo = Corrispettivo(
        canonical_id=_new_id("corr"),
        operation_id=operation_id,
        id_dispositivo=parsed.id_dispositivo,
        piva_esercente=parsed.piva_esercente,
        data_rilevazione=parsed.data_ora_rilevazione.date(),
        data_ora_rilevazione=parsed.data_ora_rilevazione.replace(tzinfo=None),
        data_ora_trasmissione=parsed.data_ora_trasmissione.replace(tzinfo=None),
        progressivo_trasmissione=parsed.progressivo_trasmissione,
        numero_doc_commerciali=parsed.numero_doc_commerciali,
        pagato_contanti=parsed.pagato_contanti,
        pagato_elettronico=parsed.pagato_elettronico,
        riepiloghi_iva=[r.to_dict() for r in parsed.riepiloghi_iva],
        source=source,
        source_external_id=f"{parsed.id_dispositivo}:{parsed.data_ora_rilevazione.date().isoformat()}",
        file_hash=file_hash,
    )
    db.add(corrispettivo)
    db.flush()

    descrizione = f"Corrispettivi {parsed.id_dispositivo} del {parsed.data_ora_rilevazione.date().isoformat()}"

    if parsed.pagato_contanti > 0:
        scritture_contabili.registra_movimento(
            db,
            conto=Conto.cassa,
            tipo=TipoMovimento.entrata,
            importo=parsed.pagato_contanti,
            data=parsed.data_ora_rilevazione.date(),
            descrizione=descrizione,
            source="corrispettivo_rt",
            operation_id=operation_id,
            source_external_id=f"{corrispettivo.source_external_id}:contanti",
            documento_id=corrispettivo.canonical_id,
            stato=StatoMovimento.confermato,
        )

    if parsed.pagato_elettronico > 0:
        scritture_contabili.registra_movimento(
            db,
            conto=Conto.banca,
            tipo=TipoMovimento.entrata,
            importo=parsed.pagato_elettronico,
            data=parsed.data_ora_rilevazione.date(),
            descrizione=f"{descrizione} — credito POS atteso",
            source="corrispettivo_rt",
            operation_id=operation_id,
            source_external_id=f"{corrispettivo.source_external_id}:elettronico",
            documento_id=corrispettivo.canonical_id,
            stato=StatoMovimento.attesa,
        )

    return corrispettivo


def elimina_corrispettivo(db: Session, *, canonical_id: str) -> bool:
    """Annulla una giornata importata per errore: rimuove la giornata e le
    scritture di Prima Nota collegate (stesso operation_id). Ritorna False se
    la giornata non esiste."""
    corrispettivo = db.scalar(select(Corrispettivo).where(Corrispettivo.canonical_id == canonical_id))
    if corrispettivo is None:
        return False

    db.execute(delete(PrimaNotaMovimento).where(PrimaNotaMovimento.operation_id == corrispettivo.operation_id))
    db.delete(corrispettivo)
    db.flush()
    return True
