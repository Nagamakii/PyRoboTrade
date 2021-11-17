#py -3 -m venv .venv
#.venv\scripts\activate
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

import os
import numpy as np
import pandas as pd
import requests as rq
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
load_dotenv()

key_id = os.getenv("APCA_API_KEY_ID")
secret_id = os.getenv("APCA_API_SECRET_KEY")
base_url = os.getenv("APCA_API_BASE_URL")

api = tradeapi.REST(key_id=key_id,secret_key=secret_id,base_url=base_url,api_version='v2')
account = api.get_account()
print(account)