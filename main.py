#py -3 -m venv .venv
#.venv\scripts\activate
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

import numpy as np
import pandas as pd
import requests as rq
import os
from dotenv import load_dotenv

load_dotenv

API = os.getenv("TEST")
print(API)