import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Global Inflation Tracker")

try:
    df = pd.read_csv("data/global_inflation.csv")
    fig = px.line(df, x="Year", y="Inflation", color="Country",
                  title="Global Inflation Comparison")
    st.plotly_chart(fig, use_container_width=True)
except:
    st.warning("Dataset not found. Please upload global_inflation.csv.")
