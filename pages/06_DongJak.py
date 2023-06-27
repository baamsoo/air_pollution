# pollution.py (동작구 2017-03-03의 시간별 오염도)
import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_folium import st_folium
import folium
import common


# 전체 데이터 읽어들이기
common.page_config()

st.title("2017-03-03 Dongjak-gu Pollution Level")

df = common.get_sales()
df['Measurement date'] = df['Measurement date'].astype('str')
df_date =df['Measurement date'].str.split(" ",n=1,expand=True) # 바로 데이터프레임의 컬럼으로 생성 expand=True

df['date'] = df_date[0]
df['time'] = df_date[1].str.slice(stop=2)
df = df.drop(['Measurement date'],axis = 1)

condition = (df['date'] == '2017-03-03')
df_birth = df[condition]

address_fixed = df["Address"].unique()[-6]

condition = (df_birth.Address == address_fixed)
df_add = df_birth[condition]

df_add = df_add.loc[:,['SO2','NO2','O3','CO','PM10','PM2.5','time']]

X_sj = df_add['time']
Y_sj = df_add['PM10']
Y2_sj = df_add['PM2.5']
Y3_sj = df_add['SO2']
Y4_sj = df_add['NO2']
Y5_sj = df_add['O3']
Y6_sj = df_add['CO']

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["PM10","PM2.5","SO2", "NO2","O3","CO"])

with tab1:
    # PM10
    plt.figure(figsize = (12,10))
    plt.bar(X_sj,Y_sj,color = 'pink')
    # x축 레이블과 사이 간격 조정
    plt.title('PM10',fontsize = 20)
    plt.xlabel('Time',fontsize=15)
    plt.xticks(rotation=30, ha='right')
    plt.ylabel('Concentration',fontsize = 15)
    st.pyplot(plt)


with tab2:
    # PM2.5
    plt.figure(figsize = (12,10))
    plt.bar(X_sj,Y2_sj,color = 'orange')
    plt.title('PM2.5',fontsize = 20)
    plt.xlabel('Time',fontsize=15)
    plt.xticks(rotation=30, ha='right')
    plt.ylabel('Concentration',fontsize = 15)
    st.pyplot(plt)
    ## 플레이데이터 주변 시간별 미세먼지 그래프

with tab3:
    # SO2
    plt.figure(figsize = (12,10))
    plt.bar(X_sj,Y3_sj,color = 'gray')
    plt.title('SO2',fontsize = 20)
    plt.xlabel('Time',fontsize=15)
    plt.xticks(rotation=30, ha='right')
    plt.ylabel('Concentration',fontsize = 15)
    st.pyplot(plt)
    ## 플레이데이터 주변 시간별 미세먼지 그래프

with tab4:
    # NO2
    plt.figure(figsize = (12,10))
    plt.bar(X_sj,Y4_sj,color = 'lightskyblue')
    plt.title('NO2',fontsize = 20)
    plt.xlabel('Time',fontsize=15)
    plt.xticks(rotation=30, ha='right')
    plt.ylabel('Concentration',fontsize = 15)
    st.pyplot(plt)
    ## 플레이데이터 주변 시간별 미세먼지 그래프

with tab5:
    # O3
    plt.figure(figsize = (12,10))
    plt.bar(X_sj,Y5_sj,color = 'rosybrown')
    plt.title('O3',fontsize = 20)
    plt.xlabel('Time',fontsize=15)
    plt.xticks(rotation=30, ha='right')
    plt.ylabel('Concentration',fontsize = 15)
    st.pyplot(plt)
    ## 플레이데이터 주변 시간별 미세먼지 그래프

with tab6:
    # CO
    plt.figure(figsize = (12,10))
    plt.bar(X_sj,Y6_sj,color = 'yellowgreen')
    plt.title('CO',fontsize = 20)
    plt.xlabel('Time',fontsize=15)
    plt.xticks(rotation=30, ha='right')
    plt.ylabel('Concentration',fontsize = 15)
    st.pyplot(plt)
    ## 플레이데이터 주변 시간별 미세먼지 그래프# pollution.py (동작구 2017-03-03의 시간별 오염도)