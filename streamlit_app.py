import time
import streamlit as st
import pandas as pd
from Bias import BiasClass

st.title("Trade Bias")

coins = sorted(["ETHUSDT", "AAVEUSDT", "SOLUSDT", "COMPUSDT", "BNBUSDT", "BTCUSDT", "BCHUSDT", "GNOUSDT"])
BC = BiasClass(coins)

Time = []
coin = []
bs = []
tc = []
data = {"Time": Time,
            "Crypto_Currency": coin,
            "Bias_score": bs,
            "Trade_Condition": tc,
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
    
    data["Time"] = Time.append(formatted_time)
    data["Crypto_Currency"] = coin.append(coins[i])
    data["Bias_score"] = bs.append(BC.bias_count(i))
    data["Trade_Condition"] = tc.append(trade_condition)
    
    st.write(f"{coins[i]} bias score: {BC.bias_count(i)}")
    
    
    
#df = pd.DataFrame(data)

#df.to_csv('bias_record.csv', index=False)

st.table(data)

#time.sleep(20)
#st.rerun()
