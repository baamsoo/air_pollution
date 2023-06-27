import streamlit as st
import common
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import pandas as pd


common.page_config()
st.title("Average PM10 for all districts (2017-2019) Visualization")

lineplot_df = common.get_sales()
lineplot_df['Measurement date'] = pd.to_datetime(lineplot_df['Measurement date'])
lineplot_df.set_index('Measurement date', inplace=True)
lineplot_df.drop(["SO2", "NO2", "O3", "CO", "PM2.5"], axis=1, inplace=True)

lineplot_df["Year"] = lineplot_df.index.year
lineplot_df["Month"] = lineplot_df.index.month

lineplot_df["Year and Month"] = lineplot_df[["Year", "Month"]].astype(str).agg("-".join, axis=1)
lineplot_df["PM10avg"] = lineplot_df.groupby(["Year and Month"])["PM10"].transform("mean")

lineplot_df.drop_duplicates(subset="Year and Month", inplace=True)

fig, ax = plt.subplots(figsize=(20, 10), constrained_layout=True)
fig.suptitle("Average PM10 for all districts (2017-2019)", fontsize=20, fontweight="bold")
lp = sns.lineplot(x=lineplot_df["Year and Month"], y=lineplot_df["PM10avg"], sort=False, ax=ax)
lp.set_ylabel("Average PM10", fontsize=20)
lp.set_xlabel("Year and Month", fontsize=20)
lp.set_xticklabels(lineplot_df["Year and Month"].values, rotation=40, ha="right")

# Streamlit 앱에 그래프 출력
st.pyplot(fig)
