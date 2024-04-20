import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import ta

url = 'https://api.upstox.com/v2/historical-candle/NSE_INDEX|Nifty 50/day/2024-04-20/2023-04-20'
flock_url = 'https://api.flock.com/hooks/sendMessage/524b8519-9a8f-4ef0-85e6-67321ae7adf9'

headers = {
    'Accept': 'application/json'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    data = data['data']['candles']
    temp = []
    temp1 = []
    for i in data:
        temp.append(i[4])
        temp1.append(i[0][0:10])
    temp.reverse()
    temp1.reverse()

    df=pd.DataFrame()
    df['Date'] = pd.DataFrame(temp1)
    df['Close'] = pd.DataFrame(temp)

    rsi = ta.momentum.RSIIndicator(df['Close']).rsi()
    df['rsi'] = rsi
    # myobj = {'text': df.to_json(orient='values')}
    # print(myobj)
    # x = requests.post(flock_url,data=json.dumps(myobj))

    ax1 = plt.subplot2grid((10,1), (0,0), rowspan = 4, colspan = 1)
    ax2 = plt.subplot2grid((10,1), (5,0), rowspan = 4, colspan = 1)

    ax1.plot(df['Close'], linewidth=2)
    ax1.set_title('Nifty Close Price')
    ax2.set_title('Relative Strength Index')
    ax2.plot(rsi, color='orange', linewidth=1)

    # Add two horizontal lines, signalling the buy and sell ranges.
    # Oversold
    ax2.axhline(20, linestyle='--', linewidth=1.5, color='green')
    # Overbought
    ax2.axhline(80, linestyle='--', linewidth=1.5, color='red')
    plt.savefig('test.png')

else:
    print(f"Error: {response.status_code} - {response.text}")
