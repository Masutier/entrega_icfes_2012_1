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



def wrongColeM():
    # ESTU F EN COLE M
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    DM_wrongColeM = data[(data['ESTU_GENERO'] == 'F') & (data['IDCOLGEN'] == "M")]
    DM_wrongColeM.to_csv('./DMs/DM_wrongColeM.csv')


def wrongColeF():
    # ESTU M EN COLE F
    data = pd.read_csv('./DMs/TH_SB11_2012_1.csv', low_memory=False)
    DM_wrongColeF = data[(data['ESTU_GENERO'] == 'M') & (data['IDCOLGEN'] == "F")]
    DM_wrongColeF.to_csv('./DMs/DM_wrongColeF.csv')
