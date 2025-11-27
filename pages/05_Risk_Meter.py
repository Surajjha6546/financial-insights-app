import streamlit as st
import pandas as pd

st.title("⚠️ Economic Risk Meter (Risco Meter)")

st.subheader("Risk Score Calculation")

cpi = st.slider("Inflation Score", 0, 100, 50)
liq = st.slider("Liquidity Score", 0, 100, 50)
vol = st.slider("Volatility Score", 0, 100, 50)
rate = st.slider("Interest Rate Pressure", 0, 100, 50)

score = 0.4*cpi + 0.3*liq + 0.2*vol + 0.1*rate

st.metric("Final Risk Score", f"{round(score,2)} / 100")

if score < 40:
    st.success("Low Risk")
elif score < 70:
    st.warning("Moderate Risk")
else:
    st.error("High Risk")
