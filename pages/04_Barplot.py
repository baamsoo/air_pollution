import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import common

common.page_config()
st.title("Top 10 pollutants by region")
df = common.get_sales()

# SO2 barplot
SO2 = df.sort_values(by = ['SO2'], ascending=False)
SO2_Address = df.groupby('Address').agg({'SO2' : 'median'}).sort_values('SO2',ascending=False).reset_index()
# Address를 기준으로 그룹화하여 SO2 집단별 평균으로 내림차순으로 정렬
# reset_index -> 인덱스 리셋(단순한 정수 인덱스로 세팅)
# 상위 10개 데이터만 저장
SO2 = SO2_Address.sort_values('SO2',ascending=False).head(10)

 # NO2 barplot
NO2 = df.sort_values(by = ['NO2'], ascending=False)
NO2_Address = df.groupby('Address').agg({'NO2' : 'median'}).sort_values('NO2',ascending=False).reset_index()
# Address를 기준으로 그룹화하여 NO2 집단별 평균으로 내림차순으로 정렬
# reset_index -> 인덱스 리셋(단순한 정수 인덱스로 세팅)
# 상위 10개 데이터만 저장
NO2 = NO2_Address.sort_values('NO2',ascending=False).head(10)

# O3 barplot
O3 = df.sort_values(by = ['O3'], ascending=False)
O3_Address = df.groupby('Address').agg({'O3' : 'median'}).sort_values('O3',ascending=False).reset_index()
# Address를 기준으로 그룹화하여 O3 집단별 평균으로 내림차순으로 정렬
# reset_index -> 인덱스 리셋(단순한 정수 인덱스로 세팅)
# 상위 10개 데이터만 저장
O3 = O3_Address.sort_values('O3',ascending=False).head(10)

# CO barplot
CO = df.sort_values(by = ['CO'], ascending=False)
CO_Address = df.groupby('Address').agg({'CO' : 'median'}).sort_values('CO',ascending=False).reset_index()
# Address를 기준으로 그룹화하여 CO 집단별 평균으로 내림차순으로 정렬
# reset_index -> 인덱스 리셋(단순한 정수 인덱스로 세팅)
# 상위 10개 데이터만 저장
CO = CO_Address.sort_values('CO',ascending=False).head(10)

# PM10 barplot
PM10 = df.sort_values(by = ['PM10'], ascending=False)
PM10_Address = df.groupby('Address').agg({'PM10' : 'median'}).sort_values('PM10',ascending=False).reset_index()
# Address를 기준으로 그룹화하여 PM3 집단별 평균으로 내림차순으로 정렬
# reset_index -> 인덱스 리셋(단순한 정수 인덱스로 세팅)
# 상위 10개 데이터만 저장
PM10 = PM10_Address.sort_values('PM10',ascending=False).head(10)

# PM2.5 barplot
PM2_5 = df.sort_values(by = ['PM2.5'], ascending=False)
PM2_5_Address = df.groupby('Address').agg({'PM2.5' : 'median'}).sort_values('PM2.5',ascending=False).reset_index()
# Address를 기준으로 그룹화하여 PM2.5 집단별 평균으로 내림차순으로 정렬
# reset_index -> 인덱스 리셋(단순한 정수 인덱스로 세팅)
# 상위 10개 데이터만 저장
PM2_5 = PM2_5_Address.sort_values('PM2.5',ascending=False).head(10)

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(['SO2', 'NO2 ', 'O3', 'CO ', 'PM10 ', 'PM2.5'])

with tab1:
  st.write('SO2 비율이 높은 정보 10개 출력')
  plt.figure(figsize=(12,40))
  sns.barplot(y="Address", x="SO2", data = SO2_Address.head(10))
  st.pyplot(plt)
with tab2:
  st.write('NO2 비율이 높은 정보 10개 출력')
  plt.figure(figsize=(12,40))
  plt.subplot(6,1,1)
  sns.barplot(y="Address", x="NO2", data = NO2_Address.head(10))
  st.pyplot(plt)
with tab3:
  st.write('O3 비율이 높은 정보 10개 출력')
  plt.figure(figsize=(12,40))
  plt.subplot(6,1,1)
  sns.barplot(y="Address", x="O3", data = O3_Address.head(10))
  st.pyplot(plt)
with tab4:
  st.write('CO 비율이 높은 정보 10개 출력')
  plt.figure(figsize=(12,40))
  plt.subplot(6,1,1)
  sns.barplot(y="Address", x="CO", data = CO_Address.head(10))
  st.pyplot(plt)
with tab5:
  st.write('PM10 비율이 높은 정보 10개 출력')
  plt.figure(figsize=(12,40))
  plt.subplot(6,1,1)
  sns.barplot(y="Address", x="PM10", data = PM10_Address.head(10))
  st.pyplot(plt)
with tab6:
  st.write('PM2.5 비율이 높은 정보 10개 출력')
  plt.figure(figsize=(12,40))
  plt.subplot(6,1,1)
  sns.barplot(y="Address", x="PM2.5", data = PM2_5_Address.head(10))
  st.pyplot(plt)
