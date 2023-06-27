# app.py (메인)
import streamlit as st
import common

common.page_config()

st.title("air pollution")
st.caption("""
"air pollution" (미세먼지와 오염물질의 상관관계):
이 데이터 세트는 대한민국 서울의 대기 오염 측정 정보를 다루고 있습니다.
미세먼지, 초미세먼지, 산소포화도, 이산화질소, 오존, 일산화탄소를 이용하여 다양한 시각화를 통해
지도를 통한 지역별 초미세먼지 농도와 각 오염물질과 미세먼지의 상관관계를 분석할 수 있습니다.
""")
st.image("img/air2.jpg")
