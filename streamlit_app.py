import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime


st.title("🎈 백종원 메이커!")
st.write(
    "백종원 메이커에 오신걸 환영합니다."
    "요리 어렵지 않습니다."
)

mbti = st.selectbox(
    "어떤 종류의 요리를 좋아하시나요?",
    ("한식", "중식", "양식", "잡식"))

if mbti == "한식":
    st.write("한식데이터")
elif mbti == "중식": 
    st.write("중식데이터")
elif mbti == "양식": 
    st.write("양식데이터")
elif mbti == "잡식": 
    st.write("돼지새끼")

