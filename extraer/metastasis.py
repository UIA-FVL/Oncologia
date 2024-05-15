# Funciones para extraer información a partir de diagnosticos oncológicos
# Autor: Quantil
# Version: 0.0.3 - 10 de junio de 2020

import re
import extraer.auxiliares as ax
from extraer.primarias import ex_organo_primario

# * Ganglios linfáticos regionales examinados y positivos
rx_ganglios = re.compile(r"ganglios?( linf[aá]ticos?| centinelas?)?", re.I)


def ganglios(registro, verbose=False):
    """
    Registra el número total de ganglios linfáticos regionales que fueron
    examinados por el patólogo y el número de ellos que fueron encontrados
    positivos para metástasis.
    @ registro: es una fila de un data frame que debe contener
    topografia, procedimiento, micro, macro y diagnóstico
    """
    # No Aplica para biopsias, citometrías y citologías
    proc = registro.procedimiento
    if proc.startswith(("1", "2")):
        return ("NA", "NA")

    topo = registro.topografia
    if rx_ganglios.search(topo):
        return ("", "")

    texto = registro.micro
    if not rx_ganglios.search(texto):
        texto = registro.diagnostico

    if not rx_ganglios.search(texto):
        return ("", "")

    if verbose:
        print("Inicia el conteo\n")
    examinados, positivos = [], []

    # primero buscamos los numero s acompañados
    ambos = re.finditer(r"(\d+)\s*/\s*(\d+)", texto)
    for m in ambos:
        txt = ax.ventana(texto, m.start(), m.end(), 3, 1, sep=r"\n+|[.:]")
        if verbose:
            print("\nHe encontrado {} \n".format(m.group()))
            print(txt)

        chk = rx_ganglios.search(txt)
        if chk:
            if verbose:
                print("\nSon ", chk.group(), " a sumarlos\n")

            positivos.append(m.group(1))
            examinados.append(m.group(2))

    # ahora los buscamos de a uno
    uno = re.finditer(r"[^\w.(/](\d+)[^/\w)%.]", texto, re.M)
    for m in uno:
        txt = ax.ventana(texto, m.start(), m.end(), 6, 4, sep=r"\s+")
        n = m.group(1)
        if verbose:
            print("\nHe encontrado {} \n".format(n))
            print(txt)

        chk = rx_ganglios.search(txt)
        if chk:
            if verbose:
                print("\nSon ", chk.group())

            exa = re.search("evaluados|examinados|negativos| sin ", txt, re.I)
            pos = re.search("positivos| con |comprometidos", txt, re.I)
            if exa:
                examinados.append(n)
                if verbose:
                    print(" Evaluados, a sumarlos\n")
            elif pos:
                positivos.append(n)
                if verbose:
                    print(" Positivos, a sumarlos\n")
            else:
                if verbose:
                    print(" Pero no sé que paso, no haré nada.\n")

    examinados = sum([int(x) for x in examinados])  # '; '.join(examinados)
    positivos = sum([int(x) for x in positivos])  # '; '.join(positivos)
    return examinados, positivos


# * Metástasis
rx_metastasis = re.compile(r"met[aá]st[aá]s\w+", re.I)


def metastasis(registro):
    """
    Esta no es una variable definitiva de la base.
    Es una variable de apoyo para obtener el órgano
    donde hay metástasis en caso de haber.
    Para correr esta función debe existir
    la columna de procedimiento.
    @ registro: es una fila de un data frame que debe contener
    las columnas micro, macro y diagnóstico
    To-Do: Se debe buscar palabras que nieguen la metástasis.
    Se debe asegurar el órgano donde ocurre.
    """
    if re.search("^[234]", registro.procedimiento):
        result = False

    texto = "\n\n\n".join([registro.diagnostico, registro.micro, registro.macro])

    # texto = texto.lower()

    if re.search(rx_metastasis, texto):
        result = []
        it = re.finditer(rx_metastasis, texto)
        for m in it:
            txt = ax.ventana(texto, m.start(), m.end(), 4, 4, sep=r"\n+|[.:]")
            result.append(txt)
        result = "\n\n\n".join(result)
    else:
        result = False

    return str(result)


def ex_metastasis(patron):
    def verificar_metastasis(registro, re=re, ax=ax):
        procedimiento = registro.procedimiento
        texto = registro.metastasis
        topografia = registro.topografia

        if re.search(pattern=patron, string=topografia):
            return "8: no aplicable"

        if procedimiento.startswith("2") or texto == "False":
            return "9: se desconoce"
        elif re.search(patron, texto):
            it = re.finditer(pattern=patron, string=texto)
            for m in it:
                txt = ax.ventana(texto, m.start(), m.end(), 4, 4, sep=r"\s+")
                if re.search("negativo|sin", txt, re.I):
                    return "0: no metástasis"
            return "1: metastasís"
        else:
            return "9: se desconoce"

    return verificar_metastasis


rx_hueso = re.compile("hueso|ost?e[ao]", re.I)
hueso = ex_metastasis(rx_hueso)
rx_cerebro = re.compile("cerebro|cerebral|cereb|encefalo", re.I)
cerebro = ex_metastasis(rx_cerebro)
rx_pulmon = re.compile("pulm[óo]n|neumo", re.I)
pulmon = ex_metastasis(rx_pulmon)
rx_higado = re.compile("h[ií]gado|hepat", re.I)
higado = ex_metastasis(rx_higado)

rx_metas = [rx_hueso, rx_ganglios, rx_pulmon, rx_cerebro, rx_higado]


def distantes(registro):
    if (registro.examinados not in ["NA", ""]) or (
        registro.positivos not in ["NA", ""]
    ):
        return "9: se desconoce"
    else:
        return (ex_metastasis(rx_ganglios))(registro)


def otras(registro):
    """
    Esta función retorna un 1 si hay metastasis en un sitio,
    no referenciado por las variables anteriores.
    Para correr esta función debe existir la columna metastasis
    creada a partir de la función metastasis().
    Para correr esta función debe existir la columna de topografia
    @ registro: es una fila de un data frame que debe contener
    las columnas micro, macro y diagnóstico
    """

    if re.search(string=registro.procedimiento, pattern="^[234]") or (
        registro.metastasis == "False"
    ):
        return "9: se desconoce"
    texto = registro.metastasis
    (topos, pris, ls) = ex_organo_primario(texto)
    for organo in topos:
        if organo not in registro.topografia:
            if any(bool(re.search(pat, organo)) for pat in rx_metas):
                pass
            else:
                return (ex_metastasis(organo))(registro)
    return "9: se desconoce"
