import streamlit as st
import common
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import pandas as pd

common.page_config()
st.title("PM10 Distribution by Top 5 Cities")
data1 = common.get_sales()

fig, ax = plt.subplots(figsize=(10,6))
PM10_Address = data1.groupby('Address').agg({'PM10': 'median'}).sort_values('PM10').reset_index()
PM10 = PM10_Address.sort_values('PM10').head(10)

PM2_5_Address = data1.groupby('Address').agg({'PM2.5': 'median'}).sort_values('PM2.5').reset_index()
PM2_5 = PM2_5_Address.sort_values('PM2.5').head(10)

SO2_Address = data1.groupby('Address').agg({'SO2': 'median'}).sort_values('SO2').reset_index()
SO2 = SO2_Address.sort_values('SO2').head(10)

NO2_Address = data1.groupby('Address').agg({'NO2': 'median'}).sort_values('NO2').reset_index()
NO2 = NO2_Address.sort_values('NO2').head(10)

O3_Address = data1.groupby('Address').agg({'O3': 'median'}).sort_values('O3').reset_index()
O3 = O3_Address.sort_values('O3').head(10)

CO_Address = data1.groupby('Address').agg({'CO': 'median'}).sort_values('CO').reset_index()
CO = CO_Address.sort_values('CO').head(10)

top_10 = pd.concat([PM10, PM2_5, SO2, NO2, O3, CO])

plt.style.use('fivethirtyeight')
fig,ax=plt.subplots(figsize=(15,8))
clr = ("blue", "forestgreen", "gold", "red", "purple",'cadetblue','hotpink','orange','darksalmon','brown')
top_10.Address.value_counts().sort_values(ascending=False)[:10].sort_values().plot(kind='barh',color=clr)
ax.set_title("Top 10 Cities",size=20)
ax.set_xlabel('Count',size=18)
st.pyplot(fig)

count=top_10['Address'].value_counts()
groups=list(top_10['Address'].value_counts().index)[:10]
counts=list(count[:10])
counts.append(count.agg(sum)-count[:10].agg('sum'))
groups.append('Other')
type_dict=pd.DataFrame({"group":groups,"counts":counts})
clr1=('brown','darksalmon','orange','hotpink','cadetblue','purple','red','gold','forestgreen','blue','plum')

qx = type_dict.plot(kind='pie', y='counts', labels=groups,colors=clr1,autopct='%1.1f%%', pctdistance=0.9, radius=1.2)
plt.legend(loc=0, bbox_to_anchor=(1.15,0.4))
plt.subplots_adjust(hspace=0.5)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10,6))
sns.kdeplot(data1[data1.Address=='136, Hannam-daero, Yongsan-gu, Seoul, Republic of Korea'].PM10,color='maroon',label='Hannam-daero')
sns.kdeplot(data1[data1.Address=='426, Hakdong-ro, Gangnam-gu, Seoul, Republic of Korea'].PM10,color='black',label='Hakdong-ro')
sns.kdeplot(data1[data1.Address=='369, Yongmasan-ro, Jungnang-gu, Seoul, Republic of Korea'].PM10,color='blue',label='Yongmasan-ro')
sns.kdeplot(data1[data1.Address=='49, Samyang-ro 139-gil, Gangbuk-gu, Seoul, Republic of Korea'].PM10,color='green',label='Samyang-ro')
sns.kdeplot(data1[data1.Address=='43, Cheonho-daero 13-gil, Dongdaemun-gu, Seoul, Republic of Korea'].PM10,color='yellow',label='Choenho-daero')
plt.title('PM10 Distribution by Top 5 Cities')
plt.legend(loc=0, bbox_to_anchor=(1.15,0.4))
plt.xlim(0,100)

st.pyplot(fig)
