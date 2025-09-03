import time
import streamlit as st
import pandas as pd
from Bias import BiasClass
from streamlit_autorefresh import st_autorefresh

# Refresh every minute
st_autorefresh(interval= 60000, key="refresh")

now = time.localtime()
hour = time.strftime("%H:%M", now)

st.title(f"Crypto Coin Strength Meter \n Time: {hour}")

# Load existing CSV from local
file_name = "dataset/bias_record.csv"
df = pd.read_csv(file_name).drop_duplicates()

if hour == "07:00" or  hour == "19:00":
    
    key = st.secrets["key"]
    secret = st.secrets["secret"]
    
    # Prepare new data
    data = {
        "Crypto_Currency": [],
        "Strength": [],
        "Trade_Condition": [],
        "Time":[],
    }

    # Coins and Bias class
    coins = sorted(["ETHUSDT", "AAVEUSDT", "SOLUSDT", "COMPUSDT", "BNBUSDT", "BTCUSDT", "BCHUSDT", "XRPUSDT", "LTCUSDT","XMRUSDT"])
    BC = BiasClass(key,secret,coins)
    
    for i in range(len(coins)):
    
        formatted_time = time.strftime("%H:%M %d/%m/%Y", now)
    
        Strength = BC.bias_count(i)
        if Strength > 0:
            trade_condition = "Strong Buy" if Strength > 100 else "Weak Buy"
        elif Strength < 0:
            trade_condition = "Strong sell" if Strength < -100 else "Weak Sell"
        else:
            trade_condition = "Not Available"
            
        data["Crypto_Currency"].append(coins[i])
        data["Strength"].append(Strength)
        data["Trade_Condition"].append(trade_condition)
        data["Time"].append(formatted_time)

    # Merge with old data
    data = pd.DataFrame(data)
    df = pd.concat([data, df], ignore_index=True).drop_duplicates()
    
    # Save locally
    df.to_csv(file_name, index=False)

else:
    st.write("WAITING ...")
    st.write("Trade bias is every 12 hours")

st.table(df)