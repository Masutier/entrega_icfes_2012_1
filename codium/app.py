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
from aux import createDM, prBxPlt
from mmm import foundMedia, foundMediana, foundModa  # Need data and column name
from db import createTable, loadTableData


def readAndClean():
    data = pd.read_csv('./docs/SB11-20121-RGSTRO-CLFCCN-V1-0-txt.csv', low_memory=False)
    # ***  ELIMINAR COLUMNAS Q NO SE VAN A USAR
    columnsrem = ['ESTU_TIPO_DOCUMENTO', 'ESTU_PAIS_RESIDE', 'ESTU_GENERO', 'ESTU_NACIMIENTO_DIA', 'ESTU_NACIMIENTO_MES', 'ESTU_NACIMIENTO_ANNO', 'ESTU_EDAD', 'FECHA_ANO', 'EDAD', 'ESTU_COD_RESIDE_MCPIO', 'ESTU_RESIDE_MCPIO', 'ESTU_RESIDE_DEPTO', 'COLE_NOMBRE_SEDE', 'COLE_CALENDARIO', 'COLE_GENERO', 'COLE_NATURALEZA', 'COLE_BILINGUE', 'COLE_CARACTER', 'PUNT_MATEMATICAS', 'PUNT_INGLES', 'DESEMP_INGLES', 'ESTU_PUESTO']

    for column in data.columns:
        if column not in columnsrem:
            data.drop([column], axis=1, inplace=True)
            data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)

    return data


def dmTdoc():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data['ESTU_TIPO_DOCUMENTO'] = data.ESTU_TIPO_DOCUMENTO.fillna('T')
    DA={'NOMBRE':data['ESTU_TIPO_DOCUMENTO']}
    newFile = "DM_TDOC"
    idCol = "IDTDOC"
    createDM(DA, newFile, idCol)

    data.columns = data.columns.str.replace('ESTU_TIPO_DOCUMENTO', 'IDTDOC')
    data['IDTDOC'] = data.IDTDOC.replace('C', int(1), regex=False)
    data['IDTDOC'] = data.IDTDOC.replace('R', int(2), regex=False)
    data['IDTDOC'] = data.IDTDOC.replace('T', int(3), regex=False)
    data['IDTDOC'] = data.IDTDOC.replace('E', int(4), regex=False)
    data['IDTDOC'] = data.IDTDOC.replace('Q', int(5), regex=False)
    data['IDTDOC'] = data.IDTDOC.replace('V', int(6), regex=False)
    data['IDTDOC'] = data.IDTDOC.replace('P', int(7), regex=False)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)
    # prBxPlt(data, idCol)

    creatableQuery = f"""CREATE TABLE IF NOT EXISTS DM_TDOC (
                    IDTDOC INTEGER PRIMARY KEY,
                    NOMBRE TEXT
                );"""
    createTable(creatableQuery)
    loadTableData(newFile)


def correctColCarac():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data['COLE_CARACTER'] = data.COLE_CARACTER.fillna('X')
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == ' INSTITUTO SURAMERICANO SIMON BOLIVAR - SEDE PRINCIPAL'), 'COLE_CARACTER_II'] = "ACADEMICO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'COLEGIO CORPORACION IBEROAMERICANA'), 'COLE_CARACTER_II'] = "ACADEMICO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'INSTITUCION EDUCATIVA SAN ANDRES'), 'COLE_CARACTER_II'] = "ACADEMICO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'INSTITUCION DE EDUCACION MEDIA EXTRANJERA'), 'COLE_CARACTER_II'] = "DESCONOCIDO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'INSTITUCION NO REGISTRADA'), 'COLE_CARACTER_II'] = "DESCONOCIDO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'PENDIENTE POR DEFINIR NOMBRE'), 'COLE_CARACTER_II'] = "DESCONOCIDO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'VALIDACION BACHILLERATO ICFES'), 'COLE_CARACTER_II'] = "DESCONOCIDO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'COL  DE LAS AMERICAS                                                                                '), 'COLE_CARACTER_II'] = "ACADEMICO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'COL NUESTRA SEÃ�ORA DEL ROSARIO'), 'COLE_CARACTER_II'] = "ACADEMICO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'INSTITUCION EDUCATIVA CUARTA POZA DE MANGA'), 'COLE_CARACTER_II'] = "ACADEMICO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'COLEGIO NUESTRA SEÃ‘ORA DE FATIMA'), 'COLE_CARACTER_II'] = "ACADEMICO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'INSTITUTO INTEGRADO ANTONIO NARIÃ‘O'), 'COLE_CARACTER_II'] = "ACADEMICO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == "KWE`SX NASA KSXA' WNXI"), 'COLE_CARACTER_II'] = "ACADEMICO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'INSTITUTO TÃ‰CNICO JOSÃ‰ MIGUEL SILVA PLAZAS'), 'COLE_CARACTER_II'] = "TECNICO"
    data.loc[(data['COLE_CARACTER'] == 'X') & (data['COLE_NOMBRE_SEDE'] == 'INSTITUTO TÃ‰CNICO OCUPACIONAL ITO - SEDE PRINCIPAL'), 'COLE_CARACTER_II'] = "TECNICO"
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)

    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data.loc[data['COLE_CARACTER_II'] == 'ACADEMICO', 'COLE_CARACTER'] = "ACADEMICO"
    data.loc[data['COLE_CARACTER_II'] == 'DESCONOCIDO', 'COLE_CARACTER'] = "DESCONOCIDO"
    data.loc[data['COLE_CARACTER_II'] == 'TECNICO', 'COLE_CARACTER'] = "TECNICO"
    data.loc[data['COLE_CARACTER'] == 'X', 'COLE_CARACTER'] = "DESCONOCIDO"
    data.drop(['COLE_CARACTER_II'], axis=1, inplace=True)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)


def dmColCarac():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    DA = {'NOMBRE': data['COLE_CARACTER']}
    newFile = "DM_COLCARAC"
    idCol = "IDCOLCARAC"
    createDM(DA, newFile, idCol)

    data.columns = data.columns.str.replace('COLE_CARACTER', 'IDCOLCARAC')
    data['IDCOLCARAC'] = data.IDCOLCARAC.str.replace(r'^(ACADEMICO)$', '1', regex=True)
    data['IDCOLCARAC'] = data.IDCOLCARAC.str.replace(r'^(ACADEMICO Y TECNICO)$', '2', regex=True)
    data['IDCOLCARAC'] = data.IDCOLCARAC.str.replace(r'^(TECNICO)$', '3', regex=True)
    data['IDCOLCARAC'] = data.IDCOLCARAC.str.replace('NORMALISTA', '4', regex=False)
    data['IDCOLCARAC'] = data.IDCOLCARAC.str.replace('DESCONOCIDO', '5', regex=True)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)
    # prBxPlt(data, idCol)

    creatableQuery = f"""CREATE TABLE IF NOT EXISTS DM_COLCARAC (
                    IDCOLCARAC INTEGER PRIMARY KEY,
                    NOMBRE TEXT
                );"""
    createTable(creatableQuery)
    loadTableData(newFile)


def dmColnatu():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data['COLE_NATURALEZA'] = data.COLE_NATURALEZA.fillna('N')
    DA = {'NOMBRE': data['COLE_NATURALEZA']}
    newFile = "DM_COLNATU"
    idCol = "IDCOLNATU"
    createDM(DA, newFile, idCol)

    data.columns = data.columns.str.replace('COLE_NATURALEZA', 'IDCOLNATU')
    data['IDCOLNATU'] = data.IDCOLNATU.str.replace('O', '1', regex=False)
    data['IDCOLNATU'] = data.IDCOLNATU.str.replace('N', '2', regex=False)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)
    # prBxPlt(data, idCol)

    creatableQuery = f"""CREATE TABLE IF NOT EXISTS DM_COLNATU (
                    IDCOLNATU INTEGER PRIMARY KEY,
                    NOMBRE TEXT
                );"""
    createTable(creatableQuery)
    loadTableData(newFile)


def dmColBilin():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data['COLE_BILINGUE'] = data.COLE_BILINGUE.fillna('X')
    dataX = data[data["COLE_BILINGUE"] == 'X']
    nans = len(dataX.index)
    dataX['aux'] = 0
    countX = len(dataX.index)
    count = len(data.index) - countX
    data0 = data[data["COLE_BILINGUE"] == 0]
    count0 = len(data0.index)
    data1 = data[data["COLE_BILINGUE"] == 1]
    count1 = len(data1.index)
    p0 = round((count0 * 100) / count)
    change0 = round((nans * p0) / 100)
    p1 = round((count1 * 100) / count)
    change1 = round((nans * p1) / 100)
    dataX['aux'] = range(1, nans + 1)

    for i in range(1,int(change0) + 1):
        dataX.loc[dataX['aux'] == i, 'COLE_BILINGUE'] = 0

    for i in range(int(change0), int(countX) + 1):
        dataX.loc[dataX['aux'] == i, 'COLE_BILINGUE'] = 1

    data = data.drop(data[data['COLE_BILINGUE'] == "X"].index)
    data = pd.concat([data, dataX])

    DA = {'NOMBRE': data['COLE_BILINGUE']}
    newFile = "DM_COLBILIN"
    idCol = "IDCOLBILIN"
    createDM(DA, newFile, idCol)
    data.columns = data.columns.str.replace('COLE_BILINGUE', 'IDCOLBILIN')
    data.drop(['aux'], axis=1, inplace=True)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)
    # prBxPlt(data, idCol)

    creatableQuery = f"""CREATE TABLE IF NOT EXISTS DM_COLBILIN (
                    IDCOLBILIN INTEGER PRIMARY KEY,
                    NOMBRE TEXT
                );"""
    createTable(creatableQuery)
    loadTableData(newFile)


def dmPuntIngles():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data['DESEMP_INGLES'] = "1"
    data['PUNT_INGLES'] = data.PUNT_INGLES.replace(-1, 0, regex=False)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)


def groupIngles():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data.loc[(data['PUNT_INGLES'] >= 0) & (data['PUNT_INGLES'] <= 15), 'DESEMP_INGLES'] = 'A-'
    data.loc[(data['PUNT_INGLES'] >= 16) & (data['PUNT_INGLES'] <= 30), 'DESEMP_INGLES'] = 'A1'
    data.loc[(data['PUNT_INGLES'] >= 31) & (data['PUNT_INGLES'] <= 45), 'DESEMP_INGLES'] = 'A2'
    data.loc[(data['PUNT_INGLES'] >= 46) & (data['PUNT_INGLES'] <= 60), 'DESEMP_INGLES'] = 'B1'
    data.loc[(data['PUNT_INGLES'] >= 61) & (data['PUNT_INGLES'] <= 75), 'DESEMP_INGLES'] = 'B2'
    data.loc[(data['PUNT_INGLES'] >= 76) & (data['PUNT_INGLES'] <= 90), 'DESEMP_INGLES'] = 'C1'
    data.loc[(data['PUNT_INGLES'] >= 91) & (data['PUNT_INGLES'] <= 100), 'DESEMP_INGLES'] = 'C2'
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)


def dmDeIngles():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    DA = {'NOMBRE': data['DESEMP_INGLES']}
    newFile = "DM_DESING"
    idCol = "IDDESING"
    createDM(DA, newFile, idCol)

    data.columns = data.columns.str.replace('DESEMP_INGLES', 'IDDESING')
    data['IDDESING'] = data.IDDESING.str.replace('A-', '1', regex=False)
    data['IDDESING'] = data.IDDESING.str.replace('A1', '2', regex=False)
    data['IDDESING'] = data.IDDESING.str.replace('A2', '3', regex=False)
    data['IDDESING'] = data.IDDESING.str.replace('B1', '4', regex=False)
    data['IDDESING'] = data.IDDESING.str.replace('B2', '5', regex=False)
    data['IDDESING'] = data.IDDESING.str.replace('C1', '6', regex=False)
    data['IDDESING'] = data.IDDESING.str.replace('C2', '7', regex=False)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)

    creatableQuery = f"""CREATE TABLE IF NOT EXISTS DM_DESING (
                    IDDESING INTEGER PRIMARY KEY,
                    NOMBRE TEXT
                );"""
    createTable(creatableQuery)
    loadTableData(newFile)


def paisRess():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    DA = {'NOMBRE': data['ESTU_PAIS_RESIDE']}
    newFile = "DM_EPAIS"
    idCol = "IDEPAIS"
    createDM(DA, newFile, idCol)

    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data.columns = data.columns.str.replace('ESTU_PAIS_RESIDE', 'IDEPAIS')
    data['IDEPAIS'] = data.IDEPAIS.fillna('CO')
    pais = pd.read_csv('./DMs/DM_EPAIS.csv', low_memory = False)
    z1 = pais['IDEPAIS']
    z2 = pais['NOMBRE']
    for idpais, nombre in zip(z1, z2):
        data['IDEPAIS'] = data.IDEPAIS.replace(nombre, idpais, regex = True)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)

    creatableQuery = f"""CREATE TABLE IF NOT EXISTS DM_EPAIS (
                    IDEPAIS INTEGER PRIMARY KEY,
                    NOMBRE TEXT
                );"""
    createTable(creatableQuery)
    loadTableData(newFile)


def coleCalen():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data = data.drop('COLE_NOMBRE_SEDE', axis=1)
    DA = {'NOMBRE': data['COLE_CALENDARIO']}
    newFile = "DM_COLCALEN"
    idCol = "IDCOLCALEN"
    createDM(DA, newFile, idCol)

    data.columns = data.columns.str.replace('COLE_CALENDARIO', 'IDCOLCALEN')
    data['IDCOLCALEN'] = data.IDCOLCALEN.fillna('4')
    data['IDCOLCALEN'] = data.IDCOLCALEN.replace("A", '1', regex=False)
    data['IDCOLCALEN'] = data.IDCOLCALEN.replace("B", '2', regex=False)
    data['IDCOLCALEN'] = data.IDCOLCALEN.replace("F", '3', regex=False)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)

    creatableQuery = f"""CREATE TABLE IF NOT EXISTS DM_COLCALEN (
                    IDCOLCALEN INTEGER PRIMARY KEY,
                    NOMBRE TEXT
                );"""
    createTable(creatableQuery)
    loadTableData(newFile)


def genero():
    # cambiar EST_GENERO cuando es "X" pero COLE_GENERO es "F" o "M"
    count = 0
    count1 = 0
    male = 0
    feme = 0
    countmale = 0
    countfeme = 0

    with open('./DMs/TH_SB11_2012_1.csv', 'r') as readFile, open('./DMs/SB11_2012_1X.csv', 'w') as writeFile: 
        fileone = csv.reader(readFile)
        headers = next(fileone)
        writer = csv.writer(writeFile)
        writer.writerow(headers)
        for row in fileone:
            if row[2] == "M":       # row[2] es ESTU_GENERO
                male += 1
                writer = csv.writer(writeFile)
                writer.writerow(row)

            if row[2] == "F":
                feme += 1
                writer = csv.writer(writeFile)
                writer.writerow(row)

            if row[2] == "X":
                if row[13] == "M":  # row[13] es COLE_GENERO
                    row[2] = "M"
                    count1 += 1
                    writer = csv.writer(writeFile)
                    writer.writerow(row)
                elif row[13] == "F":
                    row[2] = "F"
                    count1 += 1
                    writer = csv.writer(writeFile)
                    writer.writerow(row)
                else:
                    count += 1
                    writer = csv.writer(writeFile)
                    writer.writerow(row)
   
        malepor = math.ceil((male * 100) // count)  # porcentage de ESTU_GENERO con "M"
        femepor = math.ceil((feme * 100) // count)  # porcentage de ESTU_GENERO con "F"
        maletot = (count * malepor) // 100          # porcentage de casos "X" para ser asignados con "M"
        femetot = (count * femepor) // 100          # porcentage de casos "X" para ser asignados con "F"

    path = "./DMs/"
    os.remove('./DMs/TH_SB11_2012_1.csv')
    old_name = r"SB11_2012_1X.csv"
    new_name = r"TH_SB11_2012_1.csv"
    os.rename(path + old_name, path + new_name)
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)

    return maletot, femetot     # la funcion entrega estos datos cuando es llamada


def replaceGenX():
    maletot, femetot = genero()     # se llama la funcion genero() para obtener los porcentages
    count = 0
    countmale = 0
    countfeme = 0

    with open('./DMs/TH_SB11_2012_1.csv', 'r') as readFile, open('./DMs/SB11_2012_1X.csv', 'w') as writeFile: 
        fileone = csv.reader(readFile)
        headers = next(fileone)
        writer = csv.writer(writeFile)
        writer.writerow(headers)

        for row in fileone:         # bucle o "loop"
            if row[2] == "X":       # solo registros row[2] es ESTU_GENERO con "X"
                count += 1
                if maletot >= 0:    # el loop corre hasta completar porcentage de "M"
                    row[2] = "M"
                    maletot -= 1
                    countmale += 1
                    writer = csv.writer(writeFile)
                    writer.writerow(row)
                elif femetot >= 0:  # el loop corre hasta completar porcentage de "F"
                    row[2] = "F"
                    femetot -= 1
                    countfeme += 1
                    writer = csv.writer(writeFile)
                    writer.writerow(row)
            else:
                writer = csv.writer(writeFile)
                writer.writerow(row)            # se guardan los row con datos para no perderlos

    path = "./DMs/"
    os.remove('./DMs/TH_SB11_2012_1.csv')
    old_name = r"SB11_2012_1X.csv"
    new_name = r"TH_SB11_2012_1.csv"
    os.rename(path + old_name, path + new_name)


def fechas():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    datetest = datetime.strptime('15/4/2012', '%d/%m/%Y')
    # FECHAS
    Year = int(datetest.strftime('%Y'))
    month = datetest.strftime('%m')
    day = datetest.strftime('%d')

    data['ESTU_NACIMIENTO_DIA'] = data['ESTU_NACIMIENTO_DIA'].fillna(day)
    data['ESTU_NACIMIENTO_MES'] = data['ESTU_NACIMIENTO_MES'].fillna(month)
    data['ESTU_NACIMIENTO_ANNO'] = data['ESTU_NACIMIENTO_ANNO'].fillna(Year - data['ESTU_EDAD'])

    data['ESTU_NACIMIENTO_DIA'] = data['ESTU_NACIMIENTO_DIA'].map(int)
    data['ESTU_NACIMIENTO_MES'] = data['ESTU_NACIMIENTO_MES'].map(int)
    data['ESTU_NACIMIENTO_ANNO'] = data['ESTU_NACIMIENTO_ANNO'].map(int)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)

    with open('./DMs/TH_SB11_2012_1.csv', 'r') as readFile, open('./DMs/SB11_2012_1X.csv', 'w') as writeFile: 
        fileone = csv.reader(readFile)
        headers = next(fileone)
        writer = csv.writer(writeFile)
        writer.writerow(headers)
        for row in fileone:
            if row[5]:
                rowdate = row[3] + "/" + row[4] + "/" + row[5]
                if rowdate != "0/0/0":
                    fullDate = datetime.strptime(rowdate, '%d/%m/%Y')
                    diff = relativedelta.relativedelta(datetest, fullDate)
                    row[7] = str(fullDate)
                    row[8] = int(diff.years)
                    writer = csv.writer(writeFile)
                    writer.writerow(row)
                elif row[5] == " ":
                    row[7] = 'NA'
                    writer = csv.writer(writeFile)
                    writer.writerow(row)

    path = "./DMs/"
    os.remove('./DMs/TH_SB11_2012_1.csv')
    old_name = r"SB11_2012_1X.csv"
    new_name = r"TH_SB11_2012_1.csv"
    os.rename(path + old_name, path + new_name)


def deleteFechas():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data = data.drop(columns=['ESTU_NACIMIENTO_DIA', 'ESTU_NACIMIENTO_MES', 'ESTU_NACIMIENTO_ANNO'])
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)


def dmFecha():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    DA = {'NOMBRE': data['FECHA_ANO']}
    newFile = "DM_FECHA"
    idCol = "IDFECHA"
    createDM(DA, newFile, idCol)

    data.columns = data.columns.str.replace('FECHA_ANO', 'IDFECHA')
    data['IDEPAIS'] = data.IDEPAIS.fillna('CO')

    pais = pd.read_csv('./DMs/DM_EPAIS.csv', low_memory = False)
    z1 = pais['IDFECHA']
    z2 = pais['NOMBRE']
    for idpais, nombre in zip(z1, z2):
        data['IDFECHA'] = data.IDFECHA.str.replace(NOMBRE,str(IDFECHA), regex = False)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)

    creatableQuery = f"""CREATE TABLE IF NOT EXISTS DM_FECHA (
                    IDFECHA INTEGER PRIMARY KEY,
                    NOMBRE TEXT
                );"""
    createTable(creatableQuery)
    loadTableData(newFile)

    return data


def deleteEstuEdad():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data = data.drop('ESTU_EDAD', axis=1)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)


def mcpioDepto():
    # ESTU_RESIDE_DEPTO    ESTU_COD_RESIDE_MCPIO    ESTU_RESIDE_DEPTO
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data['ESTU_RESIDE_DEPTO'] = data['ESTU_COD_RESIDE_MCPIO'] // 1000
    data['ESTU_COD_RESIDE_MCPIO'] = data['ESTU_COD_RESIDE_MCPIO'].fillna('NA')
    data['ESTU_RESIDE_DEPTO'] = data['ESTU_RESIDE_DEPTO'].fillna('NA')

    data.columns = data.columns.str.replace('ESTU_COD_RESIDE_MCPIO', 'IDCODEMUNI')
    data.columns = data.columns.str.replace('ESTU_RESIDE_DEPTO', 'IDCODEDEPTO')
    data.drop(['ESTU_RESIDE_MCPIO'], axis=1, inplace=True)

    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)


def coleGenero():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data['COLE_GENERO'] = data.COLE_GENERO.fillna('X')
    DA = {'NOMBRE': data['COLE_GENERO']}
    newFile = "DM_COLGEN"
    idCol = "IDCOLGEN"
    createDM(DA, newFile, idCol)

    data.columns = data.columns.str.replace('COLE_GENERO', 'IDCOLGEN')
    data['IDCOLGEN'] = data.IDCOLGEN.replace("X", '1', regex=False)
    data['IDCOLGEN'] = data.IDCOLGEN.replace("F", '2', regex=False)
    data['IDCOLGEN'] = data.IDCOLGEN.replace("M", '3', regex=False)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)

    creatableQuery = f"""CREATE TABLE IF NOT EXISTS DM_COLGEN (
                    IDCOLGEN INTEGER PRIMARY KEY,
                    NOMBRE TEXT
                );"""
    createTable(creatableQuery)
    loadTableData(newFile)


def dmEstGen():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    DA = {'NOMBRE': data['ESTU_GENERO']}
    newFile = "DM_ESTGEN"
    idCol = "IDESTGEN"
    createDM(DA, newFile, idCol)

    data.columns = data.columns.str.replace('ESTU_GENERO', 'IDESTGEN')
    data['IDESTGEN'] = data.IDESTGEN.replace("F", '1', regex=False)
    data['IDESTGEN'] = data.IDESTGEN.replace("M", '2', regex=False)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)

    creatableQuery = f"""CREATE TABLE IF NOT EXISTS DM_ESTGEN (
                    IDESTGEN INTEGER PRIMARY KEY,
                    NOMBRE TEXT
                );"""
    createTable(creatableQuery)
    loadTableData(newFile)

    return data

def dmPuntMath():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data['DESEMP_MATH'] = 0
    data.loc[data['PUNT_MATEMATICAS'] > 100, 'PUNT_MATEMATICAS'] = 100
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)


def groupMath():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data.loc[(data['PUNT_MATEMATICAS'] >= 0) & (data['PUNT_MATEMATICAS'] <= 15), 'DESEMP_MATH'] = 'A-'
    data.loc[(data['PUNT_MATEMATICAS'] >= 16) & (data['PUNT_MATEMATICAS'] <= 30), 'DESEMP_MATH'] = 'A1'
    data.loc[(data['PUNT_MATEMATICAS'] >= 31) & (data['PUNT_MATEMATICAS'] <= 45), 'DESEMP_MATH'] = 'A2'
    data.loc[(data['PUNT_MATEMATICAS'] >= 46) & (data['PUNT_MATEMATICAS'] <= 60), 'DESEMP_MATH'] = 'B1'
    data.loc[(data['PUNT_MATEMATICAS'] >= 61) & (data['PUNT_MATEMATICAS'] <= 75), 'DESEMP_MATH'] = 'B2'
    data.loc[(data['PUNT_MATEMATICAS'] >= 76) & (data['PUNT_MATEMATICAS'] <= 90), 'DESEMP_MATH'] = 'C1'
    data.loc[(data['PUNT_MATEMATICAS'] >= 91) & (data['PUNT_MATEMATICAS'] <= 100), 'DESEMP_MATH'] = 'C2'
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)


def dmDeMath():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    DA = {'NOMBRE': data['DESEMP_MATH']}
    newFile = "DM_DESMATH"
    idCol = "IDDESMATH"
    createDM(DA, newFile, idCol)

    data.columns = data.columns.str.replace('DESEMP_MATH', 'IDDESMATH')
    data['IDDESMATH'] = data.IDDESMATH.str.replace('A-', '1', regex=False)
    data['IDDESMATH'] = data.IDDESMATH.str.replace('A1', '2', regex=False)
    data['IDDESMATH'] = data.IDDESMATH.str.replace('A2', '3', regex=False)
    data['IDDESMATH'] = data.IDDESMATH.str.replace('B1', '4', regex=False)
    data['IDDESMATH'] = data.IDDESMATH.str.replace('B2', '5', regex=False)
    data['IDDESMATH'] = data.IDDESMATH.str.replace('C1', '6', regex=False)
    data['IDDESMATH'] = data.IDDESMATH.str.replace('C2', '7', regex=False)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)

    creatableQuery = f"""CREATE TABLE IF NOT EXISTS DM_DESMATH (
                    IDDESMATH INTEGER PRIMARY KEY,
                    NOMBRE TEXT
                );"""
    createTable(creatableQuery)
    loadTableData(newFile)


def groupPuesto():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    data['DESEMP_PUESTO'] = 0
    data.loc[(data['ESTU_PUESTO'] >= 0) & (data['ESTU_PUESTO'] <= 150), 'DESEMP_PUESTO'] = 'A-'
    data.loc[(data['ESTU_PUESTO'] >= 151) & (data['ESTU_PUESTO'] <= 300), 'DESEMP_PUESTO'] = 'A1'
    data.loc[(data['ESTU_PUESTO'] >= 301) & (data['ESTU_PUESTO'] <= 450), 'DESEMP_PUESTO'] = 'A2'
    data.loc[(data['ESTU_PUESTO'] >= 451) & (data['ESTU_PUESTO'] <= 600), 'DESEMP_PUESTO'] = 'B1'
    data.loc[(data['ESTU_PUESTO'] >= 601) & (data['ESTU_PUESTO'] <= 750), 'DESEMP_PUESTO'] = 'B2'
    data.loc[(data['ESTU_PUESTO'] >= 751) & (data['ESTU_PUESTO'] <= 900), 'DESEMP_PUESTO'] = 'C1'
    data.loc[(data['ESTU_PUESTO'] >= 901) & (data['ESTU_PUESTO'] <= 1000), 'DESEMP_PUESTO'] = 'C2'
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)


def dmDePuesto():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    DA = {'NOMBRE': data['DESEMP_PUESTO']}
    newFile = "DM_PUESTO"
    idCol = "IDPUESTO"
    createDM(DA, newFile, idCol)

    data.columns = data.columns.str.replace('DESEMP_PUESTO', 'IDPUESTO')
    data['IDPUESTO'] = data.IDPUESTO.str.replace('A-', '1', regex=False)
    data['IDPUESTO'] = data.IDPUESTO.str.replace('A1', '2', regex=False)
    data['IDPUESTO'] = data.IDPUESTO.str.replace('A2', '3', regex=False)
    data['IDPUESTO'] = data.IDPUESTO.str.replace('B1', '4', regex=False)
    data['IDPUESTO'] = data.IDPUESTO.str.replace('B2', '5', regex=False)
    data['IDPUESTO'] = data.IDPUESTO.str.replace('C1', '6', regex=False)
    data['IDPUESTO'] = data.IDPUESTO.str.replace('C2', '7', regex=False)
    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)

    creatableQuery = f"""CREATE TABLE IF NOT EXISTS DM_PUESTO (
                    IDPUESTO INTEGER PRIMARY KEY,
                    NOMBRE TEXT
                );"""
    createTable(creatableQuery)
    loadTableData(newFile)


def cleanColumns():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    
    data = data.drop('ESTU_EDAD', axis=1)
    data = data.drop('FECHA_ANO', axis=1)
    data = data.drop('PUNT_INGLES', axis=1)
    data = data.drop('PUNT_MATEMATICAS', axis=1)
    data = data.drop('ESTU_PUESTO', axis=1)

    data.to_csv('./DMs/TH_SB11_2012_1.csv', index = False)

    return data


def saveThDb():
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    newFile = "TH_SB11_2012_1"

    # QUERY PARA CREAR TABLA DE HECHOS CON LLAVES FORANEAS
    creatableQuery = f"""CREATE TABLE IF NOT EXISTS TH_SB11_2012_1 (
                    IDTDOC INTEGER,
                    IDEPAIS INTEGER,
                    IDESTGEN INTEGER,
                    FECHA_ANO DATE,
                    EDAD INTEGER,
                    IDCODEMUNI INTEGER,
                    IDCODEDEPTO INTEGER,
                    IDCOLCALEN INTEGER,
                    IDCOLGEN INTEGER,
                    IDCOLNATU INTEGER,
                    IDCOLBILIN INTEGER,
                    IDCOLCARAC INTEGER,
                    PUNT_MATEMATICAS INTEGER,
                    PUNT_INGLES INTEGER,
                    IDDESING INTEGER,
                    ESTU_PUESTO INTEGER,

                    FOREIGN KEY (IDTDOC) REFERENCES DM_TDOC (IDTDOC),
                    FOREIGN KEY (IDEPAIS) REFERENCES DM_EPAIS (IDEPAIS),
                    FOREIGN KEY (IDESTGEN) REFERENCES DM_ESTGEN (IDESTGEN),
                    FOREIGN KEY (IDCOLCALEN) REFERENCES DM_COLCALEN (IDCOLCALEN),
                    FOREIGN KEY (IDCOLGEN) REFERENCES DM_COLGEN (IDCOLGEN),
                    FOREIGN KEY (IDCOLNATU) REFERENCES DM_COLNATU (IDCOLNATU),
                    FOREIGN KEY (IDCOLBILIN) REFERENCES DM_COLBILIN (IDCOLBILIN),
                    FOREIGN KEY (IDCOLCARAC) REFERENCES DM_COLCARAC (IDCOLCARAC)
                );"""

    createTable(creatableQuery)
    loadTableData(newFile)




# ***************************************************************************************************

# readAndClean()

# dmTdoc()
# correctColCarac()
# dmColCarac()

# dmColnatu()

# dmColBilin()
# dmPuntIngles()
# groupIngles()
# dmDeIngles()
# paisRess()
# coleCalen()
# genero()
# replaceGenX()
# fechas()
# deleteFechas()
# deleteEstuEdad()
# mcpioDepto()
# coleGenero()
# dmEstGen()

# dmPuntMath()
# groupMath()
# dmDeMath()
# groupPuesto()
# dmDePuesto()

# cleanColumns()

# saveThDb()
