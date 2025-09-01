import time
import streamlit as st
import pandas as pd
from Bias import BiasClass
from streamlit_autorefresh import st_autorefresh

# Auto-refresh every 60 seconds
st_autorefresh(interval=60000, key="refresh")

st.title("Trade Bias")

# Coins and Bias class
coins = sorted(["ETHUSDT", "AAVEUSDT", "SOLUSDT", "COMPUSDT", "BNBUSDT", "BTCUSDT", "BCHUSDT", "GNOUSDT"])
BC = BiasClass(coins)

# Load existing CSV from local or Google Drive
file_name = "dataset/bias_record.csv"

df = pd.read_csv(file_name).drop_duplicates()

# Prepare new data
data = {
    "Time": [],
    "Crypto_Currency": [],
    "Bias_score": [],
    "Trade_Condition": [],
}

for i in range(len(coins)):
    now = time.localtime()
    formatted_time = time.strftime("%d/%m/%Y", now)

    bias_score = BC.bias_count(i)
    if bias_score > 0:
        trade_condition = "buy"
    elif bias_score < 0:
        trade_condition = "sell"
    else:
        trade_condition = "No Trading"

    data["Time"].append(formatted_time)
    data["Crypto_Currency"].append(coins[i])
    data["Bias_score"].append(bias_score)
    data["Trade_Condition"].append(trade_condition)

    st.write(f"{coins[i]} bias score: {bias_score}")

# Merge with old data
data = pd.DataFrame(data)
new_df = pd.concat([df, data], ignore_index=True).drop_duplicates()

# Save locally
new_df.to_csv(file_name, index=False)
st.table(new_df)
