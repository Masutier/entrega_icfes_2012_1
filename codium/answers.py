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
# dataset
data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
# dataset de los mejores en math y en primer puesto de la general 
data_sub1 = data[(data["IDDESMATH"] == 7) & (data["IDPUESTO"] == 1)]
# dataset de los mejores en math y en primer puesto de la general 
data_sub2 = data[(data["IDDESING"] == 7) & (data["IDPUESTO"] == 1)]


# mas destacados - Hombres o Mujeres
def bestMath():
    girls = data_sub1[data_sub1["IDESTGEN"] == 1]
    count = len(girls.index)
    guys = data_sub1[data_sub1["IDESTGEN"] == 2]
    count1 = len(guys.index)

    if count > count1:
        print(count, "mujeres sobresalieron en el area de Matematicas, a diferencia de ", count1, "hombres")
    else:
        print(count1, "hombres sobresalieron en el area de Matematicas, a diferencia de ", count, "mujeres")


# El mejor Municipio
def bestMathCity():
    notdup = []
    sipdup = []
    total = []
    incity = data_sub1['IDCODEMUNI']
    for city in incity:
        if city not in notdup:
            notdup.append(city)
            sipdup.append(city)
        else:
            sipdup.append(city)

    for sip in notdup:
        elm_count = sipdup.count(sip)
        total += [(elm_count, sip)]

    total.sort()
    print("El municipio", total[-1][1], "se destaco con", total[-1][0], "de los mejores estudiantes, seguidos por,")
    print("El municipio", total[-2][1], "con", total[-2][0], "estudiantes.")
    # Edades
    edad =  data[(data["IDESTGEN"] == 2) & (data["IDDESMATH"] == 7) & (data["IDPUESTO"] == 1)]
    print("La mayor edad de los destacados fue de", max(edad['EDAD']), "y la menor de", min(edad['EDAD']))


def entidades():
    notdup = []
    sipdup = []
    caracter = []
    naturaleza = []
    incaract = data_sub1['IDCOLCARAC']
    innatura = data_sub1['IDCOLNATU']

    for city in incaract:
        if city not in notdup:
            notdup.append(city)
            sipdup.append(city)
        else:
            sipdup.append(city)

    for sip in notdup:
        elm_count = sipdup.count(sip)
        caracter += [(elm_count, sip)]

    DM_COLCARAC = pd.read_csv('./DMs/DM_COLCARAC.csv', low_memory=False)
    colcaracter = DM_COLCARAC["IDCOLCARAC"] == caracter[-1][1]

    for natura in innatura:
        if natura not in notdup:
            notdup.append(natura)
            sipdup.append(natura)
        else:
            sipdup.append(natura)

    for sip in notdup:
        elm_count = sipdup.count(sip)
        naturaleza += [(elm_count, sip)]

    DM_COLNATU = pd.read_csv('./DMs/DM_COLNATU.csv', low_memory=False)
    colnaturaleza = DM_COLNATU["IDCOLNATU"] == naturaleza[1][1]

    print("La Naturaleza del colegio que mas sobresalio fue de Naturaleza", DM_COLNATU["TYPO"][0])
    print("El caracter del colegio que mas sobresalio fue de caracter", DM_COLCARAC["NOMBRE"][0])


# mas destacados en ingles - Hombres o Mujeres
def besting():
    girls = data_sub2[data_sub2["IDESTGEN"] == 1]
    count = len(girls.index)
    guys = data_sub2[data_sub2["IDESTGEN"] == 2]
    count1 = len(guys.index)

    if count > count1:
        print(count, "mujeres sobresalieron en el area de Ingles, a diferencia de ", count1, "hombres")
    else:
        print(count1, "hombres sobresalieron en el area de Ingles, a diferencia de ", count, "mujeres")



bestMath()
bestMathCity()
entidades()
besting()
