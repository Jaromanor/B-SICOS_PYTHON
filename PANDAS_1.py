# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:27:07 2024

@author: javie
"""

import pandas as pd

# ABRIR EXCEL

cancer=pd.read_excel("breast_cancer.xlsx")

# ABRIR CSV
titanic=pd.read_csv("titanic.csv") #Si está en internet, simplemente poner link
wine_red=pd.read_csv("winequality-red.csv",sep=";")



# ABRIR JSON
#import requests
#covid= requests.get("https://api.covid19api.com/summary").json()
#date_coro=pd.DataFrame.from_dict(covid["Countries"])

covid=pd.read_csv("covid_20200430.csv")


# Información del dataframe

cancer.info()

# Resumen general estadístico

wine_red.describe() #no incluye categóricas. Se puede sacar aparte o todo
descriptivos=cancer.describe()
cancer.describe(include=object)
cancer.describe(include="all")


# Pequeña muestra del dataframe

cancer.head(10) #Primeras 10 filas. No se ven las 32 variables.
muestra=cancer.head(10) #Creamos un objeto pequeño y vamos al explorador de variables

cancer.tail() # las últimas 5 filas

## ACCESO A ELEMENTOS

### Shape es como la composición. 
cancer.shape

###Tipo o clase
type(cancer)

###Columnas del dataframe
titanic.columns
list(titanic.columns) #creamos una lista. Algo parecido en R para asignar nombres

### Índices
titanic.index

### Selecciona columna de dataframe
nombres=titanic["Name"]
nombres1=titanic.Name
nombres2=list(titanic.Name)

### Reordenar un dataframe
"""
Quiero de titanic pasar las dos primeras columnas al final.
Lo primero es crear la lista de nombres que ya se hizo
Luego hacer la operación
"""
list(titanic.columns)
titanic=titanic[['Name',
 'Sex',
 'Age',
 'Siblings/Spouses Aboard',
 'Parents/Children Aboard',
 'Fare','Survived',
  'Pclass']]

### Seleccionar más de una columna
nombre_sexo=titanic[["Name","Sex"]]


### Cambiar índices de un dataframe

"""
Vamos a cambiar el index por defecto del dataframe de cancer por lo que se ve
como id

"""

cancer.index=cancer["id"]
cancer.drop(["id"],axis=1,inplace=True) #Eliminamos la columna id porque la dejamos
# como índice


### Filtrar columnas de un dataframe

cols_cancer=list(cancer.columns)
cols_cancer.remove("radius_mean")

cancer=cancer[cols_cancer]


### Acceder a valores específicos de un dataframe

#### LOC

cancer.loc[842302]
cancer.loc[842302,"diagnosis"]


cancer.loc[[842302,842517],["diagnosis","radius_se"]]

cancer.loc[[842302,842517]]

titanic50=titanic.loc[0:49]


#### ILOC: Accedemos por posiciones

covid.iloc[0,0]

covid.iloc[:20,:4]


### Filtrando dataframes con operadores lógicos

calidad_5=wine_red["quality"]==5 #un vector lógico
registros_5=wine_red[calidad_5]



calidad_5_6=(wine_red["quality"]==5)|(wine_red["quality"]==6)
registros_5_6=wine_red[calidad_5_6]


#==============================================================================
#MEDIDAS DERIVADAS Y FUNCIONES
#==============================================================================

# La Media

wine_red.mean()
wine_red["fixed acidity"].mean()

##Formas iguales para un mismo resultado
wine_red[["fixed acidity","volatile acidity"]].mean()
wine_red.iloc[:,[0,1]].mean()
wine_red.iloc[:,0:2].mean()

# La desviación estándar

##sd de todo el dataframe
wine_red.std()
##sd de density y alcohol
wine_red[["density","alcohol"]].std()
wine_red.iloc[:,7:11].std() #Este toma varias columnas y no las dos que queremos
wine_red.iloc[:,[7,10]].std()


#Conteo de valores: columna específica
wine_red["quality"].value_counts()
titanic["Survived"].value_counts()


#Crear nuevas variables
covid["DeathRate"]=covid["TotalDeaths"]*100/covid["TotalConfirmed"]

#Ordenar ascendente y descendente
covid.sort_values("DeathRate",ascending=False)

#Reemplazar valores de una variable de un data frame
"""
Vamos a tomar la variable "Survived" del dataframe de Titanic y vamos a cambiar
los 0 y 1 por "Murió" y "Sobrevivió" respectivamente
"""
titanic["SurvivedLabel"]=titanic["Survived"].map({0:"Murió",1:"Sobrevivió"})
titanic["SurvivedLabel"].value_counts()
#titanic.drop(["Survived"],axis=1,inplace=True)


#Aplicar función sobre varias columnas
##Pasar Nombre y Sexo a Mayúsculas
name_sex=titanic[["Name","Sex"]].applymap(str.upper)

##Vamos a pasar únicamente los string de titanic a minúscula
###creamos función anónima
df_lower= lambda x:x.lower() if type(x)== str else x
###Pasamos la función anónima a applymap
titanic=titanic.applymap(df_lower)

















