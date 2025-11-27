import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💧 Liquidity Comparison: India vs USA")

try:
    df = pd.read_csv("data/liquidity_data.csv")

    fig = px.line(df, x="Date", y=["USA_Liquidity", "India_Liquidity"],
                  title="Liquidity Levels: USA vs India")
    st.plotly_chart(fig, use_container_width=True)
except:
    st.warning("liquidity_data.csv missing.")
