# Funciones para extraer información a partir de diagnosticos oncológicos
# Autor: Quantil
# Version: 0.0.3 - 10 de junio de 2020

import re
import numpy as np
import extraer.auxiliares as ax

# * Comportamiento
dicc_comp = {
    "0: Benigno": "benign(o|a)",
    "1: Borderline": "incierto|borderline",
    "2: In situ": "in situ",
    "3: Invasivo": "invasiv(o|a)|malign(o|a)|infiltrante",
}

list_comp = ax.listar_coincidencias(dicc_comp, flags=re.I)


def comportamiento(registro):
    """
    Registra el comportamiento del tumor que se reporta.
    @ registro: es una fila de un data frame que debe contener
    micro, macro y diagnóstico
    """
    texto = registro.diagnostico
    lista = list_comp(texto)
    if lista == []:
        texto = registro.micro
        lista = list_comp(texto)

    if lista == []:
        return "3: Invasivo"
    else:
        return min(list_comp(texto))


# * Grado / Diferenciación
diff = re.compile(r"\w+ (?:difer|e[sx]cin)\w+|(?:in|des)difer\w+|anapl[aá]stico", re.I)
grad = re.compile(
    r"grado(?: histol[oó]gico|global|total|nuclear)?:? (?P<g>\d|\w+)", re.I
)

dicc_diff = {
    "1: bien diferenciado": r"bien|completamente|1|I|bajo",
    "2: moderadamente diferenciado": r"moderad|2|II",
    "3: mal diferenciado": r"mal|pobremente|des|3|III|alto",
    "4: indiferenciado": r"in|anapl[aá]stico|4|IV",
}

list_diff = ax.listar_coincidencias(dicc_diff, flags=re.I)

linf = re.compile(r"c[eé]lulas?|linfo(ma|citos?|pro\w+)", re.I)
dicc_linf = {
    "5: célula T": r"\b(T|\bpre(cursora)?[-\s]T)\b",
    "6: célula B": r"\b(B|\bpre(cursora)?[-\s]B)\b",
    "7: célula nula": r"\b(nula|no T|no B)\b",
    "8: células NK": r"\b(NK|Natural killer)\b",
}
list_linf = ax.listar_coincidencias(dicc_linf)

rx_marcador = re.compile(r"(\w+)?CD(?P<n>\d+)(?P<signo>[\w+-]*)")
dicc_marcadores = {
    "5: célula T": r"(\w+)?CD(3)[\w+-]*",
    "6: célula B": r"(\w+)?CD(20|79|19)[\w+-]*",
    "8: células NK": r"(\w+)?CD(56|16)[\w+-]*",
}
list_marcadores = ax.listar_coincidencias(dicc_marcadores)


def ex_listar_marcadores(texto):
    marcadores = []
    for it, linea in ax.buscar_por_lineas(rx_marcador, texto):
        if re.search("expresa|positivo", linea):
            marcadores += [m.group() for m in it]
        else:
            marcadores += [m.group() for m in it if ("+" in m.group("signo"))]

    return marcadores


def grado(registro):
    """
    Describe el parecido del tumor con el tejido normal.
    @ registro: es una fila de un data frame que debe contener
    solido, micro, macro y diagnóstico
    """
    texto = "\n".join([registro.diagnostico, registro.micro, registro.macro])
    grados = []
    sol = registro.solido
    if sol.startswith("0"):
        for m in linf.finditer(texto):
            text = ax.primeras_palabras(texto[m.end() :], 4)
            grados += list_linf(text)
        if grados == []:
            marcadores = ex_listar_marcadores(texto)
            for mar in marcadores:
                grados += list_marcadores(mar)
    else:
        for m in diff.finditer(texto):
            grados += list_diff(m.group())
        for m in grad.finditer(texto):
            grados += list_diff(m.group("g"))

    if grados == []:
        grados.append("9: No determinado")

    return min(set(grados))


# * Método de confirmación
# para Tumores sólidos y Neoplasias hematopoyéticas y linfoides
dicc_metodo = {
    "1: Histología positiva": "tejido|(corte)? histol[oó]gico",
    "2: Citología positiva": "cito(me|l[oó])|flu(jo|ido)",
    # '': r'\binmunofeno|\bgen',
    # '5: prueba de laboratorio positiva': 'laboratorio'
}
list_metodo = ax.listar_coincidencias(dicc_metodo, re.I)
# pat_solido = re.compile('tumor|(adeno)?cacinoma', re.I)
rx_hemato = re.compile(r"linfo(ma|prolifer\w+)|hemato|leucem", re.I)


def metodo(registro):
    """
    Registra el mejor método de confirmación diagnóstica del cáncer.
    @ registro: es una fila de un data frame que debe contener
    micro, diagnóstico, morfologia y tipo_examen
    """
    morf = registro.morfologia

    if rx_hemato.search(morf):
        solido = "0: No es un tumor sólido"
        hemato = "3: Histología positiva PLUS"
    else:
        hemato = "0: No es un tumor hematolinfoide"
        tipo = str(registro.tipo_examen)
        if re.search("CITO", tipo):
            solido = "2: Citología positiva"
        else:
            texto = "\n".join([registro.diagnostico, registro.micro])
            metodos = list_metodo(texto)
            if metodos == []:
                solido = "9: Método desconocido"
            else:
                solido = min(set(metodos))  # '; '.join(set(metodos))

    return solido, hemato


# * Diagnóstico quirúrgico y procedimiento de estadificación
biopsia_plus = re.compile(
    "biopsia|incisi[óo]n|aguja|citometr[íi]a|citolog[ií]a|aspiración", re.I
)
no_primario = re.compile(r"met[aá]st[aá]s\w+", re.I)

dicc_proc = {
    "3: Solo exploracion": "scop[ií]a",
    "4: Cirugía sin biopsia": "bypass",
    "5: Cirugía con biopsia": "resecci[oó]n|tom[ií]a",
}

list_proc = ax.listar_coincidencias(dicc_proc, re.I)


def ex_procedimiento(texto):
    proc = list_proc(texto)

    if "5: Cirugía con biopsia" in proc:
        return "5: Cirugía con biopsia"
    else:
        if re.search(biopsia_plus, texto):
            if re.search(no_primario, texto):
                return "1: Biopsia NO primario"
            else:
                return "2: Biopsia sitio primario"

    if proc == []:
        return "9: no hay información"
    else:
        return "; ".join(set(proc))


def procedimiento(registro):
    """
    Identifica los procedimientos quirúrgicos positivos realizados
    para diagnosticar y / o estadificar la enfermedad en este hospital.
    @ registro: es una fila de un data frame que debe contener
    las columnas tipo_examen, micro, macro y diagnóstico
    """
    texto = "\n".join([registro.tipo_examen, registro.diagnostico])
    proce = ex_procedimiento(texto)

    if proce == "9: no hay información":
        texto = registro.macro
        proce = ex_procedimiento(texto)

    return proce


# * Invasión vascular - LYMPH
dicc_lymph = {
    "0: ausente": r"negativ(o|a)|ausente|no|\[\s+\]",
    "1: presente": r"positiv(o|a)|invadid(a|o)s?|presente|\[\s?[xX]\s?\]",
}
list_lymph = ax.listar_coincidencias(dicc_lymph, re.I)
pat_lymph = re.compile(r"vasos|canales|(linf\w+)?-?vascular:?|arterias|venas", re.I)


def lymph(registro):
    """
    Indica la presencia o ausencia de células tumorales en
    los canales linfáticos (no en los ganglios linfáticos) o en
    los vasos sanguíneos dentro del tumor primario,
    según lo notificó el patólogo al microscopio.

    @ registro: es una fila de un data frame que debe contener
    las columnas micro, macro, solido y diagnóstico

    Codificación:
    0: La invasión linfático-vascular está ausente o no está identificada
    1: La invasión linfático-vascular está presente o identificada
    8: No aplicable
    9: Se desconoce si hay invasión linfático-vascular o indeterminada
    """
    if re.search(string=registro.solido, pattern="^0"):
        return "8: No aplica"

    texto = "\n".join([registro.micro, registro.diagnostico])
    invasion = []

    for m in pat_lymph.finditer(texto):
        text = ax.primeras_palabras(texto[m.end() :], 4)
        invasion += list_lymph(text)
    if invasion == []:
        if bool(pat_lymph.search(texto)):
            invasion.append("1: presente")
        else:
            invasion.append("9: se desconoce")
    # Dudas:
    # 1. Qué órganos son no aplicables?
    # 2. Cómo se ve un "indeterminado"?
    return max(invasion)


# * Infiltración linfocitaria
dicc_linfocitaria = {
    "0: Ausente": r"\b(negativ(o|a)|ausente|no|sin|\[\s+\])\b",
    "1: Presente": r"\b(positiv(o|a)|presente|si|con|\[\s?[xX]\s?\])\b",
}
list_linfocitaria = ax.listar_coincidencias(dicc_linfocitaria, re.I)
pat_linfocitaria = re.compile(
    r"\b(infiltr\w+ linfoci\w+|linfoci\w+ infiltr\w+)\b", re.I
)


def linfocitaria(registro):
    """
    Indica la presencia o ausencia de linfocitos infilltrantes
    dentro del tumor primario, según lo notificó el patólogo al microscopio.

    @ registro: es una fila de un data frame que debe contener
    las columnas micro, macro, solido y diagnóstico
    """
    if re.search(string=registro.solido, pattern="^0"):
        return "8: No aplica"

    texto = "\n\n".join([registro.micro, registro.diagnostico])
    infiltracion = []

    for m in pat_linfocitaria.finditer(texto):
        text = ax.primeras_palabras(texto[m.end() :], 4)
        infiltracion += list_linfocitaria(text)
    if infiltracion == []:
        if bool(pat_linfocitaria.search(texto)):
            infiltracion.append("1: Presente")
        else:
            infiltracion.append("9: Se desconoce")
    return max(infiltracion)


# * Tamaño del tumor
def tamanho(row):
    """
    Este dato registra la medición más precisa de un tumor primario sólido,
    generalmente medido en la muestra de resección quirúrgica
    @ registro: es una fila de un data frame que debe contener
    las columnas solido, macro y procedimiento
    """

    if re.search(string=row.procedimiento, pattern="^[1234]") or row.solido.startswith(
        "0"
    ):
        return "NA"

    macro = str(row.macro)

    texto = macro
    texto = texto.lower()

    division = re.split(pattern="tumor|lesi[oó]n|neoplasia", string=texto, maxsplit=1)
    # Este split se hace para buscar la primera medición posterior a la palabra tumor

    if len(division) == 1:
        return ""
    else:
        extracciones = re.findall(
            pattern=r"[\d.,\s?x×]+[cm]m", string=division[1]
        )  # [\d.,]+\s?[x×]\s?[\d.,]+\s?cm

    if len(extracciones) > 0:
        extracciones = extracciones[0]
    else:
        extracciones = ""

    return str(extracciones.strip())


# * pTNM
def pTNM(registro):
    """
    Esta función retorna la Clasificación  pTNM de la AJCC 7a edición
    en caso de estar presente el registro.
    @ registro: es una fila de un data frame que debe contener
    las columnas micro, macro y diagnóstico.

    To-Do: Se debe alimentar con esta variable a las anteriores para
    verificar las extracciones
    """
    texto = "\n".join([registro.micro, registro.macro, registro.diagnostico])

    result = re.findall(pattern="p[TNM][A-z0-9]+", string=texto)

    if "pTNM" in result:
        for i in range(result.count("pTNM")):
            result.remove("pTNM")

    result = ";".join(result)

    return str(result)


# * Márgenes quirúrgicos del sitio primario
def margenes(registro):
    regex_match = r"(m[áa]rgen(es)?|bordes?) (((de )?(re)?secci[óo]n)|quir[úu]rgicos?|.*?comprometido)|membranas? adheridas?|(?<!sin )infiltraci[óo]n.*par[ée]nquima"
    # regex_negativo = r'(sin compromiso|no comprometido|libre|negativo|alejad[ao])'
    regex_positivo = r"(?<!sin )compromiso|(?<!no )comprome(te|tido)|en contacto|membranas? adheridas?|(?<!ni )(?<!no se observa )(?<!sin )(?<!sin lograrse identificar )(?<!sin aparente )infiltraci[óo]n.*par[ée]nquima"

    registro[registro.isna()] = ""

    diagnostico_match = list(
        filter(
            re.compile(regex_match).findall,
            re.split(r"\.\s+|\n|\r|-", registro.diagnostico.lower()),
        )
    )
    macro_match = list(
        filter(
            re.compile(regex_match).findall,
            re.split(r"\.\s+|\n|\r|-", registro.macro.lower()),
        )
    )
    micro_match = list(
        filter(
            re.compile(regex_match).findall,
            re.split(r"\.\s+|\n|\r|-", registro.micro.lower()),
        )
    )

    # if verbose:
    #     print(registro.tipo_examen)
    #     print('\nDiagnostico: {}'.format(registro.diagnostico))
    #     print('\nDiagnostico match: {}'.format(diagnostico_match))
    #     print('\nMacro: {}'.format(registro.macro))
    #     print('\nMacro match: {}'.format(macro_match))
    #     print('\nMicro: {}'.format(registro.micro))
    #     print('\nMicro match: {}'.format(micro_match))

    if registro.tipo_examen not in ["ESPECÍMENES QUIRÚRGICOS", "ESPECIMEN QUIRURGICO"]:
        return "9: desconocido o no aplicable"

    else:

        # diagnostico_match_negativo = list(filter(re.compile(regex_negativo).findall, diagnostico_match))
        diagnostico_match_positivo = list(
            filter(re.compile(regex_positivo).findall, diagnostico_match)
        )
        macro_match_positivo = list(
            filter(re.compile(regex_positivo).findall, macro_match)
        )
        micro_match_positivo = list(
            filter(re.compile(regex_positivo).findall, micro_match)
        )

        if np.max([len(diagnostico_match), len(macro_match), len(micro_match)]) == 0:
            return "9: desconocido o no aplicable"

        elif (len(macro_match_positivo) > 0) | (
            len(list(filter(re.compile("macro").findall, diagnostico_match_positivo)))
            > 0
        ):
            return "3: tumor residual macroscópico"

        elif (len(micro_match_positivo) > 0) | (
            len(list(filter(re.compile("micro").findall, diagnostico_match_positivo)))
            > 0
        ):
            return "2: tumor residual microscópico"

        elif len(diagnostico_match_positivo) > 0:
            return "1: tumor residual; NOS"

        else:
            return "0: sin tumor residual"
