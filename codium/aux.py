import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def createDM(DA, newFile, idCol):
    # ESTU_TIPO_DOCUMENTO
    DM_FILE = pd.DataFrame(DA)
    DM_FILE = DM_FILE.fillna('NA')
    DM_FILE.drop_duplicates(inplace=True)
    DM_FILE[idCol] = range(1, len(DM_FILE) + 1)
    DM_FILE.set_index(idCol, inplace=True)
    DM_FILE.to_csv('./DMs/' + newFile + '.csv')


def prBxPlt(data, idCol):
    df = data
    df.head()
    sns.boxplot( x = df[idCol] )
    plt.show()

