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


conn=sql3.connect("./DMs/STAR_SB11_2012_1.db")
cursor = conn.cursor()


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
def callFromDb():

    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)

    girls = data['IDESTGEN'] == 1
    print(girls)


    # sqlQuery = f"""SELECT IDESTGEN FROM TH_SB11_2012_1"""


    # cursor.execute(sqlQuery)
    # datos = cursor.fetchall()
    # conn.commit()
    # conn.close()

    # print(count(datos))
    # for dato in datos:
    #     print(dato)


callFromDb()