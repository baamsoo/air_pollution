import streamlit as st
import pandas as pd

# common.py (데이터 저장한 곳)

@st.cache_data

def get_sales():
    data = pd.read_csv("https://raw.githubusercontent.com/baamsoo/air_pollution/main/Measurement_summary.csv")
    return data

def page_config():
    st.set_page_config(
        page_title="test",
        page_icon="🌊",
    )
