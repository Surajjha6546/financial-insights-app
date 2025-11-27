import streamlit as st

st.set_page_config(
    page_title="Financial Insights App",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Financial Insights App")
st.write("An interactive multi-module financial analytics application.")

st.markdown("## 🔎 Available Modules")
st.markdown("- 🌍 Global Inflation Tracker")
st.markdown("- 🇺🇸 USA CPI Dashboard")
st.markdown("- 🇮🇳 India Inflation Dashboard")
st.markdown("- 💧 Liquidity Comparison (India vs USA)")
st.markdown("- ⚠️ Economic Risk Meter (Risco Meter)")

st.info("Use the sidebar to navigate between modules.")
