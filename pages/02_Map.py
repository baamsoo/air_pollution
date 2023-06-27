import streamlit as st
from streamlit_folium import st_folium
import folium
import common
import numpy as np
from numpy import sin, cos, arccos, pi, round

common.page_config()

st.title("Dot Map Visualization")

data = common.get_sales()

def rad2deg(radians):
    degrees = radians * 180 / pi
    return degrees

def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians

def getDistanceBetweenPointsNew(latitude1, longitude1, latitude2, longitude2):
    theta = longitude1 - longitude2
    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) + 
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )
    return round(distance * 1.609344, 2)

def color_select(x):
    if x >= 30:
        return 'red'
    elif x >= 25:
        return 'yellow'
    else:
        return 'blue'
      
seoul = folium.Map(location=[37.55138077230307, 126.98712254969668], zoom_start=12)

location = data.groupby('Station code')['PM2.5'].agg([np.mean])
location['Latitude'] = data['Latitude'].unique()
location['Longitude'] = data['Longitude'].unique()

markers = 999
loc_h = 0
loc_v = 0

for i in range(len(location)):
    folium.Circle(location=[location.iloc[i,1], location.iloc[i,2]], radius = location.iloc[i, 0]* 30, color=color_select(location.iloc[i,0]),fill_color='#ffffgg').add_to(seoul)
    if getDistanceBetweenPointsNew(37.4971850, 126.927595, location.iloc[i,1], location.iloc[i,2]) < markers :
        markers = getDistanceBetweenPointsNew(37.4971850, 126.927595, location.iloc[i,1], location.iloc[i,2])
        loc_h, loc_v = location.iloc[i,1], location.iloc[i,2]
        
folium.Marker([37.4971850, 126.927595], icon=folium.Icon(popup='Dongjak-gu', color='red', icon='glyphicon glyphicon-home')).add_to(seoul)
folium.Marker([loc_h, loc_v], icon=folium.Icon(popup='test', color='blue', icon='glyphicon glyphicon-home')).add_to(seoul)

st_folium(seoul, width=100%)
