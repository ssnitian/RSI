import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import ta

def getRSI():
    flock_url = 'https://api.flock.com/hooks/sendMessage/524b8519-9a8f-4ef0-85e6-67321ae7adf9'
    symbol_list = ['NSE_INDEX|Nifty 50','NSE_INDEX|Nifty Bank']
    payload = {
        "text": "Relative Strength Index",
        "attachments": []
    }
    for sym in symbol_list:
        payload['attachments'].append({
                "title": "From Controller",
                "description": sym,
                "views": {
                    "image": {
                        "original": {
                            "src": "https://rsi-umber.vercel.app/api/image?sym="+sym,
                            "width": 400,
                            "height": 400
                        },
                        "thumbnail": {
                            "src": "https://rsi-umber.vercel.app/api/image?sym="+sym,
                            "width": 400,
                            "height": 400
                        }
                    }
                }
            })

    print(payload)
    requests.post(flock_url,json=payload)
    return


getRSI()