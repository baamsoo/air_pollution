import streamlit as st
from datetime import datetime
import common
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
​
common.page_config()
​
st.title("Time-Pollution Material Correlation Coeff. and Heatmap")
​
df = common.get_sales()
df['Measurement date'] = pd.to_datetime(df['Measurement date'])  # 문자열을 날짜/시간 형식으로 변환
df['date'] = df.loc[:, "Measurement date"].dt.date  # 날짜 컬럼 생성
df = df.drop(['Measurement date'], axis=1)
​
df = df.groupby(['date'], as_index=False).agg({'SO2':'mean', 'NO2':'mean', 'O3':'mean', 'CO':'mean', 'PM10':'mean', 'PM2.5':'mean'})
df = df.drop(['date'], axis=1)
# Calculate Pearson's correlation coefficient
df_air = df.corr()
​
# 상관계수 히트맵
plt.figure(figsize=(12, 10))
ax = sns.heatmap(df_air, annot=True, cmap='coolwarm', annot_kws={"size": 24})
ax.xaxis.tick_top()
ax.tick_params(axis="x", labelsize=25)
ax.tick_params(axis="y", labelsize=25)
plt.title("Heatmap", fontsize=35, pad=30)
plt.tight_layout()
st.pyplot(plt)
