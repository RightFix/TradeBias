import time
import streamlit as st
import pandas as pd
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from Bias import BiasClass

# Authenticate
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Opens browser for login
drive = GoogleDrive(gauth)


st.title("Trade Bias")

coins = sorted(["ETHUSDT", "AAVEUSDT", "SOLUSDT", "COMPUSDT", "BNBUSDT", "BTCUSDT", "BCHUSDT", "GNOUSDT"])
BC = BiasClass(coins)

df = pd.read_csv("bias_record.csv")
df = df.drop_duplicates()
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

# Save to CSV locally
file_name = "bias_record.csv"
new.to_csv(file_name, index= False)   
st.table(new)

# Upload to Google Drive
file = drive.CreateFile({'title': file_name})
file.SetContentFile(file_name)
file.Upload()

time.sleep(60)
st.rerun()
