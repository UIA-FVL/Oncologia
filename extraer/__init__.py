"""
Funciones para extraer información a partir de diagnosticos oncológicos
Autor: Quantil
Version: 0.0.3 - 10 de Junio de 2020
"""
from . import auxiliares

from .complementarias import (
    comportamiento,
    grado,
    lymph,
    # linfocitaria,
    margenes,
    metodo,
    procedimiento,
    pTNM,
    tamanho,
)
from .metastasis import (
    cerebro,
    distantes,
    ganglios,
    higado,
    hueso,
    metastasis,
    otras,
    pulmon,
)
from .primarias import lateralidad, morfologia, topografia

variables_de_id = {
    "cod": "Código único",
    "fecha_nacimiento": "Fecha de nacimiento",
    "edad": "Edad",
    "val_fecha": "Fecha médico Patólogos",
    "val_operador": "Médicos Patólogos",
}

variables_a_extraer = {
    "topografia": "Topografía",
    "morfologia": "Morfología",
    "lateralidad": "Lateralidad",
    "comportamiento": "Comportamiento",
    "grado": "Grado de diferenciación",
    "lymph": "Invasión vascular",
    # "linfocitaria": "Infiltración Linfocitaria",
    "solido": "Tumores sólidos",
    "hemato": "Neoplasias hematopoyéticas y linfoides",
    "examinados": "Ganglios linfáticos regionales examinados",
    "positivos": "Ganglios linfáticos regionales positivos",
    "procedimiento": "Diagnóstico quirúrgico y proceso de estadificación",
    "tamanho": "Tamaño del tumor",
    "hueso": "Metástasis en hueso",
    "cerebro": "Metástasis en cerebro",
    "distantes": "Metástasis en ganglios linfáticos distantes",
    "higado": "Metástasis en higado",
    "pulmon": "Metástasis en pulmón",
    "otras": "Otras metástasis",
    "pTNM": "pTNM",
    "margenes": "Márgenes quirúrgicos del sitio primario",
}

variables = list(variables_de_id.keys()) + list(variables_a_extraer.keys())


def dar_formato(base):
    """
    Usar luego de extraer todas las variables
    para dar formato a una base.
    @base: es un pandas data frame que debe contener
    todas las 'variables'
    """
    base = base.reindex(columns=variables)
    base = base.rename(columns=variables_de_id)
    base = base.rename(columns=variables_a_extraer)
    return base


def todas_las_variables(base):
    """
    Crea un data frame con la información oncológica.
    @base: es un pandas data frame que debe contener
    micro, macro, diagnostico y tipo_examen.
    """
    base["topografia"] = base.apply(topografia, axis=1)
    base["morfologia"] = base.apply(morfologia, axis=1)
    base["lateralidad"] = base.apply(lateralidad, axis=1)
    base["comportamiento"] = base.apply(comportamiento, axis=1)
    base["procedimiento"] = base.apply(procedimiento, axis=1)
    base["solido"], base["hemato"] = zip(*base.apply(metodo, axis=1))
    base["grado"] = base.apply(grado, axis=1)
    base["lymph"] = base.apply(lymph, axis=1)
    # base["linfocitaria"] = base.apply(linfocitaria, axis=1)
    base["margenes"] = base.apply(margenes, axis=1)
    base["tamanho"] = base.apply(tamanho, axis=1)
    base["pTNM"] = base.apply(pTNM, axis=1)
    base["metastasis"] = base.apply(metastasis, axis=1)
    base["examinados"], base["positivos"] = zip(*base.apply(ganglios, axis=1))
    base["hueso"] = base.apply(hueso, axis=1)
    base["cerebro"] = base.apply(cerebro, axis=1)
    base["distantes"] = base.apply(distantes, axis=1)
    base["higado"] = base.apply(higado, axis=1)
    base["pulmon"] = base.apply(pulmon, axis=1)
    base["otras"] = base.apply(otras, axis=1)

    return base


def todas_las_variables_en_paralelo(base):
    """
    Crea un data frame con la información oncológica.
    @base: es un pandas data frame que debe contener
    micro, macro, diagnostico y tipo_examen.
    """
    base["topografia"] = base.parallel_apply(topografia, axis=1)
    base["morfologia"] = base.parallel_apply(morfologia, axis=1)
    base["lateralidad"] = base.parallel_apply(lateralidad, axis=1)
    base["comportamiento"] = base.parallel_apply(comportamiento, axis=1)
    base["procedimiento"] = base.parallel_apply(procedimiento, axis=1)
    base["solido"], base["hemato"] = zip(*base.parallel_apply(metodo, axis=1))
    base["grado"] = base.parallel_apply(grado, axis=1)
    base["lymph"] = base.parallel_apply(lymph, axis=1)
    # base["linfocitaria"] = base.parallel_apply(linfocitaria, axis=1)
    base["margenes"] = base.parallel_apply(margenes, axis=1)
    base["tamanho"] = base.parallel_apply(tamanho, axis=1)
    base["pTNM"] = base.parallel_apply(pTNM, axis=1)
    base["metastasis"] = base.parallel_apply(metastasis, axis=1)
    base["examinados"], base["positivos"] = zip(
        *base.parallel_apply(ganglios, axis=1))
    base["hueso"] = base.parallel_apply(hueso, axis=1)
    base["cerebro"] = base.parallel_apply(cerebro, axis=1)
    base["distantes"] = base.parallel_apply(distantes, axis=1)
    base["higado"] = base.parallel_apply(higado, axis=1)
    base["pulmon"] = base.parallel_apply(pulmon, axis=1)
    base["otras"] = base.parallel_apply(otras, axis=1)

    return base
