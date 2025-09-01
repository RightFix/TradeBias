import time
import streamlit as st
import pandas as pd
from Bias import BiasClass

df = 

st.title("Trade Bias")

coins = sorted(["ETHUSDT", "AAVEUSDT", "SOLUSDT", "COMPUSDT", "BNBUSDT", "BTCUSDT", "BCHUSDT", "GNOUSDT"])
BC = BiasClass(coins)

for i in range(len(coins)):
  st.write(f"{coins[i]} bias score: {BC.bias_count(i)}")

time.sleep(20)
st.rerun()
