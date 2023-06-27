import pandas as pd


def foundMedia(data, column):
    promedio = data['ESTU_NACIMIENTO_ANNO'].mean()
    promedio = int(promedio)

    return promedio


def foundMediana(data, column):
    median = data['ESTU_NACIMIENTO_ANNO'].median()
    median = int(median)
    data['ESTU_NACIMIENTO_ANNO'].fillna(median, inplace = True)
    print(median)

    return median


def foundModa(data, column):
    moda = data['ESTU_NACIMIENTO_ANNO'].mode()[0]
    moda = int(moda)

    return moda





