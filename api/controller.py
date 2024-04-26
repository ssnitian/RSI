import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import ta

def getRSI():
	flock_url = 'https://api.flock.com/hooks/sendMessage/524b8519-9a8f-4ef0-85e6-67321ae7adf9'
	requests.post(flock_url,data='''{
    "text": "This is a test message.",
    "attachments": [
        {
            "title": "attachment title",
            "description": "attachment description",
            "views": {
                "image": {
                    "original": {
                        "src": "https://rsi-umber.vercel.app/api/image",
                        "width": 400,
                        "height": 400
                    },
                    "thumbnail": {
                        "src": "https://rsi-umber.vercel.app/api/image",
                        "width": 400,
                        "height": 400
                    }
                }
            }
        }
    ]
}''')
	return


getRSI()