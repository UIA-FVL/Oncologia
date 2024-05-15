"""
Corpus de expresiones regulares usadas para entender textos oncológicos
"""
# Corpus de expresiones regulares usadas para entender textos oncológicos
# Autor: Quantil
# Version: 0.0.3 - 8 de junio de 2020


# Identificación de cancer:
# utilizando el diccionario enviado por la FVL
# y el diccionario que se encuentra en:
# http://www.minsa.gob.pa/sites/default/files/general/2003_clasificacion_internacional_de_enfermedades_para_oncologia_-_cie-o_3.pdf

import re

from . import morfologia as morf
from . import topografia as top

morf_primario_oma = re.compile(
    r"\b\w*(" + "|".join(morf.primario_oma) + r")\w*(o?ma)\b", re.I,
)

de = r"( (del?|de la|con|no) )?"
morf_primario_general = re.compile(
    r"\b(" + "|".join(morf.general) + r")\b" + de + r"(\w+){1,2}", re.I
)

morf_leuc = re.compile(r"(\w+ )?(" + "|".join(morf.leuc) + r")\w+", re.I)


morf_primario = [morf_primario_oma, morf_leuc, morf_primario_general]

morf_omas = re.compile(
    r"\b(" + "|".join(morf.prefijos_oma) + r")\w*(" + "|".join(morf.sufijos) + ")",
    re.I,
)
morf_raros = re.compile(r"(" + "|".join(morf.raros) + r")\w+", re.I)


morf_otros = [morf_omas, morf_raros]

tipo_hist = re.compile(
    r"("
    + "|".join(
        [
            "estudio de (?!inmunohis)",
            "tipo histol[oó]gico (del carcinoma)?",
            "tipo del? tumor",
            r"histolog[ií]a del? \w+",
        ]
    )
    + r"):?\s*",
    re.I,
)

lat_emparejado = re.compile("|".join(top.lat_emparejado), re.I)


top_primario = {
    k: re.compile(r"\w*(" + "|".join(v) + r")\b", re.I) for k, v in top.primario.items()
}


pre = r"(\b(y|del?|de la|con) )?"
top_complementario = {
    k: re.compile(pre + r"\w*(" + "|".join(v) + r")\b", re.I)
    for k, v in top.complementario.items()
}
