import sqlite3 as sql3
import pandas as pd


# Crear la Base de Datos
def createDB():
    conn=sql3.connect("./DMs/STAR_SB11_2012_1.db")
    conn.commit()
    conn.close()


def createTable(creatableQuery):
    conn=sql3.connect("./DMs/STAR_SB11_2012_1.db")
    cursor = conn.cursor()

    cursor.execute(creatableQuery)

    conn.commit()
    conn.close()


def loadTableData(newFile):
    conn=sql3.connect("./DMs/STAR_SB11_2012_1.db")
    dimen = pd.read_csv('./DMs/' + newFile + '.csv', low_memory=False)

    dimen.to_sql(newFile, conn, if_exists='append', index=False)

    conn.commit()
    conn.close()


def createFactsTable(creatableQuery):
    conn=sql3.connect("./DMs/STAR_SB11_2012_1.db")
    cursor = conn.cursor()

    cursor.execute(creatableQuery)

    conn.commit()
    conn.close()



# # Insertar csv's a la Base de Datos
# def LoadStar():
#     conn = sql3.connect("./DMs/STAR_SB11_2012_1.db")
#     dms = ['DM_TDOC', 'DM_COLNATU', 'DM_COLBILIN', 'DM_COLCARAC', 'DM_DESING', 'DM_EPAIS', 'DM_COLGEN', 'DM_wrongColeF', 'DM_wrongColeM']

#     for dm in dms:
#         data = pd.read_csv('./DMs/' + dm + '.csv', low_memory=False)
#         data.to_sql(name=dm, con=conn, if_exists="append", index=False)
        
#     conn.close()


# # Insertar csv's a la Base de Datos
# def LoadTablaHechos():
#     conn = sql3.connect("./DMs/STAR_SB11_2012_1.db")
#     data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
#     data.to_sql(name='TH_SB11_2012_1', con=conn, if_exists="append", index=False)
    
#     conn.close()