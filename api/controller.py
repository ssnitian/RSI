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
        "attachments": [
            {
                "title": "From Controller",
                "description": "NSE_INDEX|Nifty Bank",
                "views": {
                    "image": {
                        "original": {
                            "src": "https://rsi-umber.vercel.app/api/image?sym=NSE_INDEX%7CNifty%20Bank",
                            "width": 400,
                            "height": 400
                        },
                        "thumbnail": {
                            "src": "https://rsi-umber.vercel.app/api/image?sym=NSE_INDEX%7CNifty%20Bank",
                            "width": 400,
                            "height": 400
                        }
                    }
                }
            },
            {
                "title": "From Controller",
                "description": "NSE_INDEX|Nifty 50",
                "views": {
                    "image": {
                        "original": {
                            "src": "https://rsi-umber.vercel.app/api/image?sym=NSE_INDEX|Nifty 50",
                            "width": 400,
                            "height": 400
                        },
                        "thumbnail": {
                            "src": "https://rsi-umber.vercel.app/api/image?sym=NSE_INDEX|Nifty 50",
                            "width": 400,
                            "height": 400
                        }
                    }
                }
            }
        ]
    }
    requests.post(flock_url,json=payload)
    return


getRSI()