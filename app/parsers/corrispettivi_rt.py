"""Parser per gli XML ufficiali dei corrispettivi RT (Agenzia delle Entrate,
schema COR10, namespace ivaservizi.agenziaentrate.gov.it/docs/xsd/corrispettivi/dati/v1.0).

Verificato su file reali del cliente (non contiene dati di esempio inventati:
la struttura è quella confermata nei file scaricati da Drive durante la
ricognizione). Vedi docs/spec/03_PAGINE/LOGICA_JSON/06-corrispettivi.json.
"""

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from xml.etree import ElementTree as ET

NS = "http://ivaservizi.agenziaentrate.gov.it/docs/xsd/corrispettivi/dati/v1.0"


class CorrispettivoXmlError(ValueError):
    """L'XML non rispetta lo schema COR10 atteso: campo mancante o non decodificabile."""


@dataclass
class RiepilogoIVA:
    aliquota_iva: Decimal | None
    natura: str | None
    imposta: Decimal
    ammontare: Decimal
    importo_parziale: Decimal

    def to_dict(self) -> dict:
        return {
            "aliquota_iva": str(self.aliquota_iva) if self.aliquota_iva is not None else None,
            "natura": self.natura,
            "imposta": str(self.imposta),
            "ammontare": str(self.ammontare),
            "importo_parziale": str(self.importo_parziale),
        }


@dataclass
class CorrispettivoRT:
    id_dispositivo: str
    piva_esercente: str
    progressivo_trasmissione: str
    data_ora_trasmissione: datetime
    data_ora_rilevazione: datetime
    numero_doc_commerciali: int
    pagato_contanti: Decimal
    pagato_elettronico: Decimal
    riepiloghi_iva: list[RiepilogoIVA] = field(default_factory=list)


def _find_text(root: ET.Element, path: str) -> str:
    el = root.find(path)
    if el is None or el.text is None:
        raise CorrispettivoXmlError(f"campo mancante o vuoto: {path}")
    return el.text.strip()


def parse_corrispettivo_xml(xml_bytes: bytes) -> CorrispettivoRT:
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as exc:
        raise CorrispettivoXmlError(f"XML non valido: {exc}") from exc

    # Il root ha il namespace COR10 (es. <n1:DatiCorrispettivi xmlns:n1="...">),
    # ma i figli nei file reali non hanno prefisso (namespace vuoto): niente
    # namespace nelle ricerche sotto al root.
    if root.tag != f"{{{NS}}}DatiCorrispettivi":
        raise CorrispettivoXmlError(f"elemento radice inatteso: {root.tag}")

    trasmissione = root.find("Trasmissione")
    if trasmissione is None:
        raise CorrispettivoXmlError("elemento Trasmissione mancante")

    dispositivo = trasmissione.find("Dispositivo")
    if dispositivo is None:
        raise CorrispettivoXmlError("elemento Dispositivo mancante")

    dati_rt = root.find("DatiRT")
    if dati_rt is None:
        raise CorrispettivoXmlError("elemento DatiRT mancante")

    totali = dati_rt.find("Totali")
    if totali is None:
        raise CorrispettivoXmlError("elemento Totali mancante")

    riepiloghi: list[RiepilogoIVA] = []
    for riepilogo in dati_rt.findall("Riepilogo"):
        iva_el = riepilogo.find("IVA")
        natura_el = riepilogo.find("Natura")
        if iva_el is not None:
            aliquota = Decimal(_find_text(iva_el, "AliquotaIVA"))
            imposta = Decimal(_find_text(iva_el, "Imposta"))
            natura = None
        elif natura_el is not None:
            aliquota = None
            natura = natura_el.text.strip() if natura_el.text else None
            imposta = Decimal("0.00")
        else:
            raise CorrispettivoXmlError("Riepilogo senza IVA né Natura")
        riepiloghi.append(
            RiepilogoIVA(
                aliquota_iva=aliquota,
                natura=natura,
                imposta=imposta,
                ammontare=Decimal(_find_text(riepilogo, "Ammontare")),
                importo_parziale=Decimal(_find_text(riepilogo, "ImportoParziale")),
            )
        )

    return CorrispettivoRT(
        id_dispositivo=_find_text(dispositivo, "IdDispositivo"),
        piva_esercente=_find_text(trasmissione, "PIVAEsercente"),
        progressivo_trasmissione=_find_text(trasmissione, "Progressivo"),
        data_ora_trasmissione=datetime.fromisoformat(_find_text(trasmissione, "DataOraTrasmissione")),
        data_ora_rilevazione=datetime.fromisoformat(_find_text(root, "DataOraRilevazione")),
        numero_doc_commerciali=int(_find_text(totali, "NumeroDocCommerciali")),
        pagato_contanti=Decimal(_find_text(totali, "PagatoContanti")),
        pagato_elettronico=Decimal(_find_text(totali, "PagatoElettronico")),
        riepiloghi_iva=riepiloghi,
    )
