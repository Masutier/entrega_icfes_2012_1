import sqlite3 as sql3
import pandas as pd


columnsrem = [
    'ESTU_TIPO_DOCUMENTO', 'ESTU_PAIS_RESIDE', 'ESTU_GENERO', 'ESTU_NACIMIENTO_DIA'
    , 'ESTU_NACIMIENTO_MES', 'ESTU_NACIMIENTO_ANNO', 'ESTU_EDAD', 'FECHA_ANO', 'EDAD'

    , 'ESTU_LIMITA_BAJAVISION', 'ESTU_LIMITA_SORDOCEGUERA', 'ESTU_LIMITA_COGNITIVA', 'ESTU_LIMITA_INVIDENTE'
    , 'ESTU_LIMITA_MOTRIZ', 'ESTU_LIMITA_SORDOINTERPRETE', 'ESTU_LIMITA_SORDONOINTERPRETE'

    , 'ESTU_COD_RESIDE_MCPIO', 'ESTU_RESIDE_MCPIO', 'ESTU_RESIDE_DEPTO'

    , 'COLE_CALENDARIO', 'COLE_GENERO', 'COLE_NATURALEZA', 'COLE_BILINGUE', 'COLE_CARACTER'

    , 'PUNT_MATEMATICAS', 'PUNT_INGLES', 'DESEMP_INGLES', 'ESTU_PUESTO']


dimen = [
    readAndClean(),

    dmTdoc(),
    dmColnatu(),
    dmColbilin(),
    dmColcarac(),
    dmDeIngles(),

    paisRess(),
    coleCalen(),

    coleGenero(),
    genero(),
    replaceGenX(),
    dmEstGen(),

    fechas(),
    deleteFechas(),
    deleteEstuEdad(),

    mcpioDepto(),

    wrongColeM(),
    wrongColeF(),

    createDB(),
    LoadStar(),
    LoadTablaHechos()

]
