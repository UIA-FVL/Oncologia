# Funciones para extraer información a partir de diagnosticos oncológicos
# Autor: Quantil
# Version: 0.0.3 - 10 de junio de 2020

import re
import extraer.auxiliares as ax
import extraer.corpus as rx


# * Topografía sitio primario
def topografia(registro, verbose=False):
    """
    Ubica el sitio primario del cancer.
    @ registro: es una fila de un data frame que debe contener
    micro, macro y diagnóstico
    """
    texto = registro.diagnostico
    topografias, primarios, lineas = ex_organo_primario(texto)

    if primarios == []:
        texto = registro.macro
        topografias, primarios, lineas = ex_organo_primario(texto)

    if primarios == []:
        topografia = "No identificado"
        primario = ""
        contexto = ""
    else:
        primario = primarios[0]
        contexto = "\n".join(lineas)
        tokens = ax.flatten(
            [m.group().lower() for m in re.finditer(rx.top_complementario[primario], l)]
            for p, l in zip(primarios, lineas)
            if p == primario
        )
        topografia = " ".join(ax.unique(tokens)).title()

    if verbose:
        return topografia, primario, contexto
    else:
        return topografia


ex_organos_mencionados = ax.todas_las_coincidencias(rx.top_primario)


def ex_organo_primario(texto):
    """
    Extrae todos los organos mencionados en el texto,
    junto con su grupo primario y el contexto donde aprecen.
    """
    candidatos = ex_organos_mencionados(texto)
    primarios, lineas = [], []
    topografias = []

    for k, it in candidatos:
        for m in it:
            primarios.append(k)
            topografias.append(m.group())
            lineas.append(
                ax.ventana(texto, m.start(), m.end(), 1, 2, sep=r'[-",:.\n\r]')
            )

    return topografias, primarios, lineas


# * Lateralidad


def ex_lateralidad(texto):
    if re.search("derech(o|a)", texto, re.I):
        lateralidad = "1"
    elif re.search("izquierd(o|a)", texto, re.I):
        lateralidad = "2"
    else:
        lateralidad = "9"

    return lateralidad


def lateralidad(registro):
    """
    Decide la lateralidad del sitio primario del cancer.
    @ registro: es una fila de un data frame que debe contener
    topografia
    """
    # Paso 1: Intentificar si el organo es emparjado o no o es desconocido.
    topo = registro.topografia
    emparejado = re.search(rx.lat_emparejado, topo)
    if emparejado:
        # Paso 2: Identificar lateralidad
        lateral = ex_lateralidad(topo)
    else:
        lateral = "0"

    return lateral


# * Morfología
def ex_morfologia_primario(texto):
    for pat in rx.morf_primario:
        primario, linea = ax.cortar_primario(pat, texto, n=2, sep=r'[)",:.\n\r]')
        if primario:
            return primario, linea

    return None, None


def ex_morfologia_otros(texto):
    for pat in rx.morf_otros:
        m = re.search(pat, texto)
        if m:
            primario = m.group()
            linea = ax.ventana(texto, m.start(), m.end(), 1, 2, sep=r'[)",:.\n\r]')
            return primario, linea

    return None, None


def morfologia(registro, verbose=False):
    """
    Identifica la anatomía microscópica de las celulas del tumor
    @ registro: es una fila de un data frame que debe contener
    micro, macro y diagnóstico
    """
    primario = None
    micro = registro.micro
    hist, texto = ax.cortar_primario(rx.tipo_hist, micro, 3, sep=r'[)",:.\n\r]')
    if hist:
        primario, linea = ex_morfologia_primario(texto)

    if primario is None:
        diag = registro.diagnostico
        primario, linea = ex_morfologia_primario(diag)

    if primario is None:
        primario, linea = ex_morfologia_otros(diag)

    if primario is None:
        macro = registro.macro
        texto = macro + "\n\n\n\n" + micro
        primario, linea = ex_morfologia_primario(texto)

    if primario is None:
        primario, linea = ex_morfologia_otros(texto)

    if primario is None:
        morfologia = "No identificado"
        primario = ""
        contexto = ""
    else:
        primario = primario.title()
        contexto = linea
        linea = ax.limpieza(linea, kill=False)
        linea = ax.primeras_palabras(linea, 5)
        morfologia = primario + " " + linea.title()

    if verbose:
        return morfologia, primario, contexto
    else:
        return morfologia
