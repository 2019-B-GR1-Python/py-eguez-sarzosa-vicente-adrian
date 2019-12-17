# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:49:23 2019

@author: USRBET
"""

import pandas as pd

path_guardado_bin = "C://Users//USRBET//Documents//GitHub//py-eguez-sarzosa-vicente-adrian//03 - pandas//data//artwork_data_completo.pickle"

df = pd.read_pickle(path_guardado_bin)

## Obtener nombres de los artistas

serie_artistas_repetidos = df["artist"]

artistas = pd.unique(serie_artistas_repetidos)

artistas.size
len(artistas)

blake = df["artist"] == "Blake, William"

blake.value_counts()
df["artist"].value_counts()

df_blake = df[blake]












