# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:08 2019

@author: USRBET
"""
import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)
s1 = df1[0]
s2 = df1[1]
s3 = df1[2]
s1[0]

df1[3] = s1

df1[4] = s1 * s2

datos_fisicos_uno = pd.DataFrame(
        arr_pand,
        columns=[
                'Estatura (cm)',
                'Peso (kg)',
                'edad(anios)'])

datos_fisicos_dos = pd.DataFrame(
        arr_pand,
        columns=[
                'Estatura (cm)',
                'Peso (kg)',
                'edad(anios)'],
        index=['Adrian','Vicente'])

df1.index = ['Adrian', 'Vicente']
df1.index = ['Pepe', 'Vicente']
df1.columns = ['A','B','C','D','F']













