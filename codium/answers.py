import os
import csv
import math
import sqlite3 as sql3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ydata_profiling
from datetime import datetime, timedelta
from dateutil import relativedelta
from mmm import foundMedia, foundMediana, foundModa  # Need data and column name


# conn=sql3.connect("./DMs/STAR_SB11_2012_1.db")
# cursor = conn.cursor()


"""
Se desea comprobar lo siguiente:
    Quienes se destacaron mas en matemáticas, si las mujeres o los hombres, teniendo en cuenta:
        La ciudad
        Edad de acuerdo al tipo de documento de identidad
        Tipo de colegio (Oficial, Privado) 
        Caracterización del colegio (ACADEMICO, TECNICO, etc.)
        Qué nivel de ingles
        Nacionalidad
"""

# Leer db y ordenar data
def bestMath():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)

    girls = data[(data["IDESTGEN"] == 1) & (data["IDDESMATH"] == 7)]
    count = len(girls.index)

    guys = data[(data["IDESTGEN"] == 2) & (data["IDDESMATH"] == 7)]
    count1 = len(guys.index)

    if count > count1:
        print(count, "mujeres sobresalieron en el area de Matematicas, a diferencia de ", count1, "hombres")
    else:
        print(count1, "hombres sobresalieron en el area de Matematicas, a diferencia de ", count, "mujeres")


def bestMathCity():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)

    girls = data[(data["IDESTGEN"] == 1) & (data["IDDESMATH"] == 7) & (data["IDCODEMUNI"])]
    count = len(girls.index)

    guys = data[(data["IDESTGEN"] == 2) & (data["IDDESMATH"] == 7) & (data["IDCODEMUNI"])]
    count1 = len(guys.index)

    if count > count1:
        print(count, "mujeres sobresalieron en el area de Matematicas, a diferencia de ", count1, "hombres")
    else:
        print(count1, "hombres sobresalieron en el area de Matematicas, a diferencia de ", count, "mujeres")





bestMath()
bestMathCity()