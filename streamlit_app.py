import time
import streamlit as st
import pandas as pd
from Bias import BiasClass
from streamlit_autorefresh import st_autorefresh

# Refresh every minute
st_autorefresh(interval= 60000, key="refresh")

now = time.localtime()
hour = time.strftime("%H:%M", now)

st.title("Trade Bias")

# Load existing CSV from local
file_name = "dataset/bias_record.csv"
df = pd.read_csv(file_name).drop_duplicates()

if hour == "15:10" or hour == "12:00":
    
    key = st.secrets["api"]["key"]
    secret = st.secrets["api"]["secret"]
    
    # Prepare new data
    data = {
        "Crypto_Currency": [],
        "Bias_score": [],
        "Trade_Condition": [],
        "Time":[],
    }

    # Coins and Bias class
    coins = sorted(["ETHUSDT", "AAVEUSDT", "SOLUSDT", "COMPUSDT", "BNBUSDT", "BTCUSDT", "BCHUSDT", "XRPUSDT", "LTCUSDT","XMRUSDT"])
    BC = BiasClass(key,secret,coins)
    
    for i in range(len(coins)):
    
        formatted_time = time.strftime("%H:%M %d/%m/%Y", now)
    
        bias_score = BC.bias_count(i)
        if bias_score > 0:
            trade_condition = "Buy"
        elif bias_score < 0:
            trade_condition = "Sell"
        else:
            trade_condition = "Wait"
            
        data["Crypto_Currency"].append(coins[i])
        data["Bias_score"].append(bias_score)
        data["Trade_Condition"].append(trade_condition)
        data["Time"].append(formatted_time)

    # Merge with old data
    data = pd.DataFrame(data)
    df = pd.concat([df, data], ignore_index=True).drop_duplicates()
    
    # Save locally
    df.to_csv(file_name, index=False)

else:
    st.write("WAITING ...")
    st.write("Trade bias is every 12 hours")

st.table(df)