##測試CSV 端點是否也會被擋

import pandas as pd
import requests
from io import StringIO

URL = "https://rate.bot.com.tw/xrt/flcsv/0/day"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}

resp = requests.get(URL, headers=HEADERS, timeout=20)
print("狀態碼:", resp.status_code)
print("內容長度:", len(resp.text))
print(resp.text[:500])
