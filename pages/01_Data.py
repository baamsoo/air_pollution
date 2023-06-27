# Data.py (데이터 불러온 곳)
import streamlit as st
import common

common.page_config()
st.title("Data")
st.divider()
st.dataframe(common.get_sales(), use_container_width=True, hide_index=True)
