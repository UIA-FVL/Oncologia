"""
 Funciones auxiliares para la extracción de texto
 Autor: Quantil
 Version: 0.0.3 - 10 de junio de 2020
"""

from nltk.corpus import stopwords
import numpy as np
import re


def mirar_un_ejemplo(f, cols, base):
    """
    Elige una observación de la base.
    Imprime la columna junto con el resultado de aplicar la función.
    """
    i = np.random.choice(base.index)
    row = base.loc[i, cols]
    print("registro {}:\n".format(i))
    for col in cols:
        print("{}:\n{}\n\n".format(col, row.at[col]))
    print("\nResultado:\n{}".format(f(row)))


newline = re.compile(r"[.-]\W+|\n+|\r\n?|\b[A-Z][.:;-]\b")


def buscar_por_lineas(pat, texto):
    lineas = re.split(newline, texto)
    return [(re.finditer(pat, li), li) for li in lineas if re.search(pat, li)]


def todas_las_coincidencias(diccionario, flags=0):
    compilado = {k: re.compile(v, flags) for k, v in diccionario.items()}

    def f(texto):
        return [(k, v.finditer(texto)) for k, v in compilado.items() if v.search(texto)]

    return f


def listar_coincidencias(diccionario, flags=0):
    compilado = {k: re.compile(v, flags) for k, v in diccionario.items()}

    def f(texto):
        return [k for k, v in compilado.items() if v.search(texto)]

    return f


def primeras_palabras(texto, n):
    palabras = re.split(r"\s+", texto, n)[0: (n - 1)]
    return " ".join(palabras)


def ventana(texto, i_inicio, i_fin, n_pre=1, n_pos=1, sep=r"\s+", un=" ", res="**"):
    texto_pre = texto[:i_inicio]
    texto_pos = texto[i_fin:]
    return un.join(
        re.split(sep, texto_pre)[-n_pre:]
        + [res, texto[i_inicio:i_fin], res]
        + re.split(sep, texto_pos, n_pos)[:n_pos]
    )


def cortar_primario(pat, texto, n=1, sep=r"\s+", un=" "):
    m = re.search(pat, texto)
    if m:
        primario = m.group()
        linea = texto[m.end():]
        linea = un.join(re.split(sep, linea, n)[:n])
    else:
        primario = None
        linea = texto

    return primario, linea


acentos_y_puntos = str.maketrans("áéíóú", "aeiou", '.,:;-")(/%')


def limpieza(
    texto,
    stopwords=stopwords.words("spanish"),
    otherwords=["tipo", "[0-9]+"],
    kill=True,
):
    texto = texto.lower()
    if kill:
        ignorar = r"\b(" + "|".join(stopwords + otherwords) + r")\b"
        texto = re.sub(ignorar, "", texto)
    texto = re.sub(r"\W+", " ", texto)
    texto = texto.strip()  # elimina espacio end-string
    return texto


def espanhol(texto, **kwargs):
    texto = limpieza(texto, **kwargs)
    texto = texto.translate(acentos_y_puntos)
    return texto


def tokenize(texto, sep=r"[\W\s]", **kwargs):
    texto = limpieza(texto, **kwargs)
    tokens = re.split(sep, texto)
    return tokens


def flatten(lists):
    return (item for sublist in lists for item in sublist)


def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]
