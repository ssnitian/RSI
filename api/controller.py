import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import ta
from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        getRSI()
        self.send_response(200)
        self.send_header('Content-type','image/x-png')
        self.end_headers()
        with open('/tmp/test1.png', 'rb') as file:
          self.wfile.write(file.read())
        return

def getRSI():
	return