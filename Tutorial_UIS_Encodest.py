# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 11:29:08 2024

@author: javie
"""

#========================================================
#PANDAS UIS
#========================================================

import pandas as pd

titanic=pd.read_csv("titanic.csv")

titanic.values
titanic.columns
titanic.index

titanic.info()
titanic.shape
titanic.describe(include="all")

#Ordenar las filas ascendente (viene por defecto) y descendente

titanic.sort_values("Age",ascending=False) #descendente
titanic.sort_values(["Age","Pclass"],ascending=[True,False])

#Escoger columnas
titanic[["Survived","Sex"]]
