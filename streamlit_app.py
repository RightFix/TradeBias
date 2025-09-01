import time
import streamlit as st
import pandas as pd
from Bias import BiasClass



st.title("Trade Bias")

coins = sorted(["ETHUSDT", "AAVEUSDT", "SOLUSDT", "COMPUSDT", "BNBUSDT", "BTCUSDT", "BCHUSDT", "GNOUSDT"])
BC = BiasClass(coins)

for i in range(len(coins)):
    if BC.bias_count(i) > 0:
        trade_condition = "buy"
    elif BC.bias_count(i) < 0:
        trade_condition = "sell"
    else:
        "No Trading"
    st.write(f"{coins[i]} bias score: {BC.bias_count(i)}")

time.sleep(20)
st.rerun()
