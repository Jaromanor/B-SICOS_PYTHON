# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 08:22:52 2024

@author: javie
"""

import pandas as pd
import datetime

#fecchas con datetime

fecha_ejecucion=datetime.datetime.now()
print(type(fecha_ejecucion))
print(fecha_ejecucion)

##podemos acceder a los atributos del objeto "fecha_ejecución"

fecha_ejecucion.year
fecha_ejecucion.day
fecha_ejecucion.date()
str(fecha_ejecucion.date())

fecha_ejecucion.strftime("%X") ###hora
fecha_ejecucion.strftime("%x") ###fecha formato d/m/año
fecha_ejecucion.strftime("%A") ###día

fecha_ejecucion.date()+datetime.timedelta(days=10) ### sumar 10 días al objeto
str(fecha_ejecucion.date()+datetime.timedelta(days=-2))


# FECHAS CON PANDAS

## PASAR STRING A FECHA
pd.to_datetime("06/08/2024")
pd.to_datetime("2024-08-06")
pd.to_datetime("20240806")
pd.to_datetime("20241205") #año, día, mes. Pero ojo porque 12 puede ser mes
pd.to_datetime("20241205",format="%Y%d%m") # arreglado como quiero

energy=pd.read_csv("https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv")
type(energy.iloc[0,0])
energy.index=energy["Date"]
type(energy.index[0])
energy.drop("Date",axis=1,inplace=True)

energy=energy.loc["2014":] #escogemos datos desde el 2014
energy=energy.loc["2014-06":] #escogemos datos desde el 2014 pero junio
energy=energy.loc["2014-06":"2017-06"] #escogemos datos desde el 2014 pero junio hasta junio 2017

#poner el índice como columna
energy.reset_index(inplace=True)
#Fecha superior a 2015
energy["Date"]>"2015" #de esta manera me arroja un lógico
### La forma para filtrar de una vez sería
energy=energy[energy["Date"]>"2015"]

### convertir en fecha
energy["Date"]=pd.to_datetime(energy["Date"])
energy.info()

#Gráfico
energy.plot(x="Date")

#Vamos a crear la columna año"
energy["Year"]=energy["Date"].dt.year
#Vamos a crear la columna día"
energy["Day"]=energy["Date"].dt.dayofweek
#Vamos a crear la columna día pero no en número sino en nombre"
energy["Day_name"]=energy["Date"].dt.strftime("%A")

#Quitemos algunas columnas
energy=energy.drop(["Year","Day","Day_name"],axis=1)
#Vamos a mensualizar los registros: sumarlos por mes
m_energy=energy.resample("M",on="Date").sum()
m_energy.plot()























