# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:04:45 2019

@author: USRBET
"""

import pandas as pd

path_guardado_bin = "C://Users//USRBET//Documents//GitHub//py-eguez-sarzosa-vicente-adrian//03 - pandas//data//artwork_data_completo.pickle"

df = pd.read_pickle(path_guardado_bin)
df2 = df.set_index('id')
"""
NOMBRE         nota 1    disciplina
Pepito        7           5
Juanita       8           9
Maria         9           2
"""
datos = {
        "nota 1":{
                "Pepito":7,
                "Juanita":8,
                "Maria":9},
        "disciplina":{
                "Pepito":5,
                "Juanita":9,
                "Maria":2}
        }
notas = pd.DataFrame(datos)
notas.loc["Pepito"]
notas.iloc[0]
type(notas.loc["Pepito"]) # Serie

notas.loc["Pepito","disciplina"]

notas.loc["Pepito",["disciplina","nota 1"]]

notas.loc[["Pepito","Juanita"], ["nota 1"]]

notas.loc[["Pepito","Juanita"], "nota 1"]

notas.loc[[True, False, True]]

condicion_nota = notas["nota 1"] > 7
condicion_disc = notas["disciplina"] > 7

mayores_siete = notas.loc[ condicion_nota, ["nota 1"] ]

mayores_siete = notas.loc[condicion_nota][condicion_disc]

## notas.loc[condicion_nota]
## mayores_siete[condicion_disc]


notas.loc["Maria","disciplina"] = 7

# Estudiantes menores a 7 en disciplina
# Suben a 7

# Solo a pepito se le va a poner 10 en todo

# Disciplina se les baje a 7

notas.loc[:,"disciplina"] = 7

# Anadir la columna promedio nota 1 y disciplina



primero = df2.loc[0]

primero = df2.iloc[0]







































