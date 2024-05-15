"""
 Funciones para extraer marcadores biológicos para distintos grupos de tumores solidos
 Autor: Quantil
 Version: 0.0.1 - 10 de agosto de 2020
"""

import re
import extraer.auxiliares as ax

dicc_01 = {
    "0: Negativo": r"negativ(o|a)|ausente|no|sin|\[\s+\]|-",
    "1: Positivo": r"positiv(o|a)|presente|con|\[\s?[xX]\s?\]|[+]|alta",
}
list_01 = ax.listar_coincidencias(dicc_01, re.I)


def verificar_marcador(
    patron, pre=3, pos=4,
):
    """
    Crea una función usada para extraer el marcador
    """

    def ex_marcador(registro, re=re, ax=ax):
        marcador = []
        texto = "\n".join([registro.micro, registro.diagnostico])

        for m in patron.finditer(texto):
            text = ax.ventana(texto, m.start(), m.end(), pre, pos)
            marcador += list_01(text)
        if marcador == []:
            if bool(patron.search(texto)):
                marcador.append("8: Se menciona")
            else:
                marcador.append("9: Se desconoce")
        return max(marcador)

    return ex_marcador


# * Marcadores Moleculares Mama

rx_estrogeno = re.compile(r"\bestr[óo]genos?\b", re.I)
estrogeno = verificar_marcador(rx_estrogeno)

rx_prostageno = re.compile(r"\b(progesterona|prost[áa]genos?|PgR)\b", re.I)
prostageno = verificar_marcador(rx_prostageno)

rx_her2 = re.compile(r"\bHER-?2\b")
her2 = verificar_marcador(rx_her2)

rx_ki67 = re.compile(r"\bKi-?67\b")
ki67 = verificar_marcador(rx_ki67)

marcadores_mama = {
    "Estrógeno": estrogeno,
    "Prostágeno": prostageno,
    "Her2": her2,
    "Ki67": ki67,
}

# * Marcadores Gastrointestinal

rx_ras = re.compile(r"\b[KNH]R[Aa][Ss]\b")
ras = verificar_marcador(rx_ras)

rx_ims = re.compile(r"\b(IMS?|MSI|[Ii]nstabilidad (de )?[Mm]icros[aá]t[eé]lites)\b")
ims = verificar_marcador(rx_ims)

marcadores_gastro = {
    "Her2": her2,
    "Ki67": ki67,
    "Ras": ras,
    "IMS": ims,
}

# * Marcadores Pulmón

rx_egfr = re.compile(r"\b(EGFR)\b")
egfr = verificar_marcador(rx_egfr)

rx_pdl1 = re.compile(r"\b(PDL1)\b")
pdl1 = verificar_marcador(rx_pdl1)

rx_alk = re.compile(r"\b(ALK)\b")
alk = verificar_marcador(rx_alk)

marcadores_pulmon = {
    "EGRF": egfr,
    "PDL1": pdl1,
    "ALK": alk,
}

# * Marcadores otros
rx_vph = re.compile(r"\b(VPH|[pP]16)\b")
vph = verificar_marcador(rx_vph)

rx_braf = re.compile(r"\b(BRAF)\b")
braf = verificar_marcador(rx_braf)

marcadores_vph = {"VPH": vph}
marcadores_tejidos = {"BRAF": braf}
