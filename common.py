import streamlit as st
import pandas as pd

# common.py (데이터 저장한 곳)

@st.cache_data

def get_sales():
    data = pd.read_csv("https://github.com/baamsoo/air_pollution/blob/17998c4f89482385d617500c846eae49298ab3e8/Measurement_summary.csv")
    data.dropna(inplace=True)
    return data

def page_config():
    st.set_page_config(
        page_title="test",
        page_icon="🌊",
    )
