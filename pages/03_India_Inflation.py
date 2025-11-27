import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🇮🇳 India Inflation Dashboard")

try:
    df = pd.read_csv("data/india_cpi.csv")
    fig = px.line(df, x="Date", y="CPI", title="India CPI Trend")
    st.plotly_chart(fig, use_container_width=True)
except:
    st.warning("india_cpi.csv not found in data folder.")
