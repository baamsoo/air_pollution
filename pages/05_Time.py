import streamlit as st
import common
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

common.page_config()

st.title("Time-Pollution Material Concentration Plot")

df = common.get_sales()
df['Measurement date'] = pd.to_datetime(df['Measurement date'])
df['hour'] = df.loc[:, "Measurement date"].dt.hour

data = df.groupby('hour', as_index=False).agg({'SO2':'mean', 'NO2':'mean', 'O3':'mean', 'CO':'mean', 'PM10':'mean', 'PM2.5':'mean'})

fig, (ax1, ax2) = plt.subplots(figsize = (15, 15), nrows=2, ncols=1)
fig.suptitle('Time-Pollution Material Concentration Plot', fontsize=30)

y1 = ['SO2', 'NO2', 'O3']
y2 = ['PM10', 'PM2.5']
y1_label = [r'$SO_2$', r'$NO_2$', r'$O_3$']
y2_label = ['PM10', 'PM2.5']

for idx, ys1 in enumerate(y1):
    ax1.plot(data['hour'], data[ys1], label=y1_label[idx])
ax1.grid()
ax1.legend(loc="upper left", fontsize=14)
ax1.set_ylabel(r'$SO_2$, $NO_2$, $O_3$', fontsize=17)
ax1.tick_params(axis="x", labelsize=15)
ax1.tick_params(axis="y", labelsize=15)

for idx, ys2 in enumerate(y2):
    ax2.plot(data['hour'], data[ys2], label=y2_label[idx])
ax2.grid()
ax2.legend(loc="upper left", fontsize=14)
ax2.set_xlabel('Time [hour]', fontsize=17)
ax2.set_ylabel('PM10, PM2.5', fontsize=17)
ax2.tick_params(axis="x", labelsize=15)
ax2.tick_params(axis="y", labelsize=15)
fig.tight_layout()
st.pyplot(fig)
