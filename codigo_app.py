#$ pip install streamlit --upgrade
#$ pip install matplotlib

import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px

import numpy as np
import streamlit as st
from datetime import datetime

import matplotlib.pyplot as plt

from PIL import Image

import altair as alt
import urllib.request
import base64



st.title('Datos Hidrometereológicos Gobierno Regional Piura')

st.markdown("""Esta pagina web "app" exploratoria permite visualizar a cualquier usuario los datos hidrometereológicos del Gobierno Regional de Piura""")

st.header('Nosotros el Equipo 3')
st.markdown("""
           Somos un exelente grupo de estudiantes que se encuentra cursando el 5to ciclo de la carrera de Ingeniería Ambiental en la Universidad 
	   Peruana Cayetano Heredia. Como proyecto final del curso “Programación Avanzada”,realizamos esta página en base a los conocimientos 
	   adquiridos en las clases teóricas y prácticas durante del ciclo, junto a la asesoría y enseñansas de nuestros profesores.
	   """) 
image = Image.open('tenorio el papi (2).jpg')
st.image(image, caption='Futuros Ingenieros Ambientales', use_column_width=True)

st.header('Agua y saneamiento')
st.markdown("""
	Contiene los datos Hidrometeorológicos del Sistema Hidráulico Mayor a cargo del  Proyecto Especial Chira Piura.
        Este dataset muestra los datos hidrometereológicos registrados de las presas, estaciones hidrológicas e hidrométricas.
        Esta información contiene el nombre de la cuenca, nombre de la estación, medida del caudal a las 007:00 horas, el promedio del caudal a las 
	24:00 horas, el caudal máximo a las 24:00 horas, niveles de presas a las 7:00 horas, nivel máximo de las presas a las 24:00 horas, el volumen 
	de las presas a las 07:00 y precipitaciones.La cuenca es una extensión de terreno en un valle, escurren aguas formando un río atravesando valles 
	y escurriendo en el mar. Una cuenca puede tener varias estaciones hidrometeorológicas.El dato de precipitación es la lluvia acumulada entre las 
	7:00 horas del día anterior y las 7:00 horas de hoy (24 horas), cuando se considera el campo vacío, indica que no se realizaron mediciones.
	""")
st.header('Dato y Medio de Distribución')

st.markdown("""* **Datos Hidrometereológicos Gobierno Regional Piura:** https://www.datosabiertos.gob.pe/dataset/datos-hidrometereol%C3%B3gicos-gobierno-regional-piura/resource/897966b9-f582-4898-83fe""")
st.markdown("""* **Metadatos de los Datos Hidrometereológicos Gobierno Regional Piura:** https://www.datosabiertos.gob.pe/dataset/datos-hidrometereol%C3%B3gicos-gobierno-regional-piura/resource/454e8897-4e25-486e-8291""")
st.markdown("""* **Diccionario de Datos de los Datos Hidrometereológicos Gobierno Regional Piura:** https://www.datosabiertos.gob.pe/dataset/datos-hidrometereol%C3%B3gicos-gobierno-regional-piura/resource/d7437ef6-8950-4c25-bc91""")

st.markdown("""
	* **Para mayor información también puede ingresar a:** http://servicios.regionpiura.gob.pe/datosh
	""")

image = Image.open('Proyecto_Piura.jpg')
st.image(image, caption='Piura: Gobierno regional pone a disposición información hidrometeorológica del sistema hidráulico Chira - Piura', use_column_width=True)

st.header('Datos Hidrometereológicos ')

image = Image.open('crear_mapa.jpg')
st.image(image, caption='  ', use_column_width=True)




###st.sidebar.header("Entradas del usuario")
###selected_prov=st.sidebar.selectbox('Provincia', list(reversed(range(2010,2021))))




st.header("Datos Hidrometereológicos Gobierno Regional Piura")
st.markdown("""Este dataset muestra los datos hidrometereológicos registrados de las presas, estaciones hidrológicas e hidrométricas.""")
@st.experimental_memo
def download_data():
   url="https://www.datosabiertos.gob.pe/sites/default/files/DATOS_HIDROMETEREOLOGICOS_GORE_PIURA_2.csv"
   filename="DATOS_HIDROMETEREOLOGICOS_GORE_PIURA_2.csv"
   urllib.request.urlretrieve(url,filename)
   df=pd.read_csv('DATOS_HIDROMETEREOLOGICOS_GORE_PIURA_2.csv')
   return df
c=download_data()
st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
st.dataframe(c)
st.subheader("Características del Dataset")
st.write(c.describe())

#para sacar datos
datos= pd.read_csv('DATOS_HIDROMETEREOLOGICOS_GORE_PIURA_2.csv')
#st.dataframe(datos)

st.subheader('Conteo de datos en las diferente provincias de Piura')

df_anho_freq = pd.DataFrame(datos["PROVINCIA"].value_counts())
st.bar_chart(df_anho_freq)
st.header('Análisis exploratorio')

# Seleccion del dataset
st.subheader('Seleccionar los datos de las diferentes provincias de Piura')

opcion_dataset = st.selectbox(
    '¿Qué dataset de las provincias de Piura deseas visualizar?',
    ('Ayabaca','Morropon','Piura','Sullana')
    )

#DATOS DE CADA PROVINCIA
df_latlog= pd.read_csv('latylog progra.csv')
datos_Ayabaca= pd.read_csv('Ayabaca_Piura3.csv')
datos_Morropon= pd.read_csv('Morropon_Piura.csv')
datos_Piura= pd.read_csv('Piura_Piura.csv')
datos_Sullana= pd.read_csv('Sullana_Piura.csv')

df_visualizacion = None
estado = '-'

if opcion_dataset == 'Ayabaca':
    df_visualizacion = datos_Ayabaca
    estado = 'Datos de la provincia de Ayabaca'
elif opcion_dataset == 'Morropon':
    df_visualizacion = datos_Morropon
    estado = 'Datos de la provincia de Morropón'
elif opcion_dataset == 'Piura':
    df_visualizacion = datos_Piura
    estado = 'Datos de la provincia de Piura'
elif opcion_dataset == 'Sullana':
    df_visualizacion = datos_Sullana
    estado = 'Datos de la provincia de Sullana'

#Con fé dá.
st.markdown("##") # Linea en blanco
df_latlog = df_latlog.rename(columns={'latitud':'lat', 'longitud':'lon'})
st.map(df_latlog[['lat','lon']])
st.write('Figura 1. Ubicación de las centrales hidrometeorológicas.')

###

t0 = estado 
st.subheader(t0)
st.dataframe(df_visualizacion)
st.write('Figura 2. Gráfica de los datos generales de la provincia seleccionada')
st.markdown("---")

###

t1 = '• Cantidad de cuencas según los '+estado+'' 
st.subheader(t1)
df_cuenca_freq = pd.DataFrame(df_visualizacion["CUENTA"].value_counts())
st.bar_chart(df_cuenca_freq)
st.write('Figura 3. Gráfica del nombre de cuencas en la provincia seleccionada')
st.markdown("---")

###

t2 = '• Cantidad de estaciones según los '+estado+'' 
st.subheader(t2)
df_anho_freq = pd.DataFrame(df_visualizacion["ESTACION"].value_counts())
st.bar_chart(df_anho_freq)
st.write('Figura 4. Gráfica de nombre de las estaciones hidrometeorológicas en la provincia seleccionada')
st.markdown("---")

###

t3= '• Medida del caudal a las 07:00 horas según los '+estado+'' 
st.subheader(t3)
df_precip_freq = pd.DataFrame(df_visualizacion["CAUDAL07H"].value_counts())
st.line_chart(df_precip_freq)
st.write('Figura 5. Gráfica de las medidas del caudal en la provincia seleccionada')
st.markdown("---")

###

t4 = '• Porcentaje de datos en los distritos según '+estado+''
st.subheader(t4)
df_actividad_freq = pd.DataFrame(df_visualizacion["DISTRITO"].value_counts())
labels = df_actividad_freq.index.tolist()
sizes = df_actividad_freq["DISTRITO"].tolist()
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
startangle=0)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)
st.write('Figura 6. Gráfica circular del porcentaje datos en los distritos de la provincia seleccionada')
st.markdown("---")

###

t5 = '• Porcentaje del tipo de estación según los '+estado+'' 
st.subheader(t5)
df_tipo_freq = pd.DataFrame(df_visualizacion["TIPO_ESTACION"].value_counts())
labels = df_tipo_freq.index.tolist()
sizes = df_tipo_freq["TIPO_ESTACION"].tolist()
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
startangle=0, textprops={'fontsize': 10})

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)
st.write('Figura 7. Gráfica circular del porcentaje de estaciones en la provincia seleccionada')
st.markdown("---")


