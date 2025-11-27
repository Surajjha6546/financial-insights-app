import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🇺🇸 USA CPI Dashboard")

try:
    df = pd.read_csv("data/usa_cpi.csv")
    fig = px.line(df, x="Date", y="CPI", title="USA CPI Trend")
    st.plotly_chart(fig, use_container_width=True)
except:
    st.warning("usa_cpi.csv not found in data folder.")
