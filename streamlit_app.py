import streamlit as st
from Bias import BiasClass


st.title("Trade Bias")

coins = sorted(["ETHUSDT", "AAVEUSDT", "SOLUSDT", "COMPUSDT", "BNBUSDT", "BTCUSDT", "BCHUSDT", "GNOUSDT"])
BC = BiasClass(coins)

for i in range(len(coins)):
  st.write(f"{coins[i]} bias score: {BC.bias_count(i)}")

st.rerun()
