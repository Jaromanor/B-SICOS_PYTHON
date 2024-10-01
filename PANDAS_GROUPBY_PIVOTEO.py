# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 08:09:54 2024

@author: javie
"""

import pandas as pd

retail=pd.read_csv("OnlineRetail.csv",encoding="Latin1") #Tocó agregar el argumento
# enconding porque se estaba generando un problema que no reconocía un caracter

retail.info()
retail.describe()

#Conocer cantidad de nulos
retail.isna().sum()

retail.head()

#Crear variable Fecha_Mes para posteriormente agrupar mis datos
##Adecuamos la columna a formato fecha
retail["InvoiceDate"]=pd.to_datetime(retail["InvoiceDate"])
##Creamos función anónima que nos va a servir para tomar solamente los caracteres
##que necesitamos
anio_mes=lambda x:x[:7]
##Creamos
retail["Fecha_Mes"]=retail["InvoiceDate"].astype(str).map(anio_mes)

#Cálculo del monto de la venta

retail["Total_Ventas"]=retail["Quantity"]*retail["UnitPrice"]
muestra=retail.sample(5000)

##Vamos a escoger las ventas mayores que cero
retail=retail[retail["Total_Ventas"]>0]
muestra=retail.sample(5000)

# ¿Cuál es el monto de ventas histórico por mes?
"""
La variable de agregación es "Fecha Mes", pasamos el argumento as_index=False
para que la variable no quede como índice. El método agg sirve para saber qué
sobre qué variable se va a realizar la agregación y qué acción.
"""
ventas_mes=retail.groupby(["Fecha_Mes"],as_index=False).agg({"Total_Ventas":"sum"})
ventas_mes.plot(x="Fecha_Mes")

# ¿Cuál es el monto de las ventas histórico mensual por país?
ventas_mes_pais=retail.groupby(["Fecha_Mes","Country"],as_index=False).agg({"Total_Ventas":"sum"})

# ¿Cuál es el número de órdenes histórico mensual por país

N_ordenes = retail.groupby(["Fecha_Mes","Country"],as_index=False).agg({"InvoiceNo":"nunique"})


# Histórico de ventas de manera amigable "tidy"

ventas_productos=retail.pivot_table(index="StockCode",columns=["Fecha_Mes"],values="Total_Ventas",aggfunc="sum")
"""
Quedaron muchos nan que en realidad deben ser ceros. Representan que no hubo ventas
en ese mes de ese producto. Para ello se agrega el argumento fill_value=0 a la función
"""
ventas_productos=retail.pivot_table(index="StockCode",columns=["Fecha_Mes"],values="Total_Ventas",aggfunc="sum",fill_value=0)

# Haga un pivote de las ventas mensuales por país, para que cada país sea una columna

ventas_pais=ventas_mes_pais.pivot_table(index="Fecha_Mes",columns=["Country"],values="Total_Ventas",aggfunc="sum",fill_value=0)



#==================
#Despivoteo-Melt
#==================

vp=pd.read_excel("venta_productos.xlsx")

##Creamos una lista con todos los nombres de las columnas de vp excepto "producto"
valores=[col for col in vp.columns if col!="Producto"]
##dESPIVOTEO
vp_despivoteo=pd.melt(vp,id_vars=["Producto"],value_vars=valores)
##cambiamos esos nombres
vp_despivoteo=pd.melt(vp,id_vars=["Producto"],value_vars=valores,value_name="Piezas",var_name="anio_mes")



#=====================================
#EXPORTAR NUESTRAS DATAS
#=====================================

vp_despivoteo.to_csv("exportación.csv")
vp_despivoteo.to_excel("exportación.xlsx",index=False,sheet_name="La Cartilla")










