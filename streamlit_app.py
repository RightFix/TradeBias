import time
import streamlit as st
import pandas as pd
from Bias import BiasClass

st.title("Trade Bias")

coins = sorted(["ETHUSDT", "AAVEUSDT", "SOLUSDT", "COMPUSDT", "BNBUSDT", "BTCUSDT", "BCHUSDT", "GNOUSDT"])
BC = BiasClass(coins)

df = pd.read_csv("dataset/bias_record.csv")
data = { "Time": [],
    "Crypto_Currency" :[],
    "Bias_score" :[],
    "Trade_Condition" :[],
}

for i in range(len(coins)):
    now = time.localtime()
    formatted_time = time.strftime("%H:%M %d %m %Y", now)
    if BC.bias_count(i) > 0:
        trade_condition = "buy"
    elif BC.bias_count(i) < 0:
        trade_condition = "sell"
    else:
        trade_condition = "No Trading"
    
    data["Time"].append(formatted_time)
    data["Crypto_Currency"].append(coins[i])
    data["Bias_score"].append(BC.bias_count(i))
    data["Trade_Condition"].append(trade_condition)

    st.write(f"{coins[i]} bias score: {BC.bias_count(i)}")
 
data = pd.DataFrame(data)   
new  = pd.concat([df, data], ignore_index = True)
new.to_csv("dataset/bias_record.csv", index= False)   
st.table(new)

time.sleep(60)
st.rerun()
