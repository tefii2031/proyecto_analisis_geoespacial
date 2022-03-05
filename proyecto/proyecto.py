"""Tarea 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/161YdXmre5OWCn3D7Ik8Qqxcs55R8PQUG

#Tarea 03 - Análisis de datos geoespaciales mediante pandas, plotly, geopandas y folium

## Estudiantes:

Daniel Salazar Mora - B87214
Stephanie María Leitón Ramírez - B74106

##Importando las bibliotecas
"""

import math
import streamlit as st
import pandas as pd
import geopandas as gpad
import plotly.express as px
import folium
from folium import Marker
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap

from streamlit_folium import folium_static
#
# Configuración de la página
#
