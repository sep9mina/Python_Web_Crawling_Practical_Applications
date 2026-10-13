import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
resp = requests.get(url)

# 1. 觀察 Header 與編碼資訊
content_type = resp.headers.get("Content-Type", "")
print(f"Content-Type 標頭 : {content_type}")
print(f"resp.encoding : {resp.encoding}")
print(f"apparent_encoding : {resp.apparent_encoding}")

# 2. 原始預設解碼 (會出現 Â£ 亂碼)
soup_wrong = BeautifulSoup(resp.text, "html.parser")
price_wrong = soup_wrong.select_one(".price_color").text
print(f"[亂碼] 價格 = {price_wrong}")

# 3. 修法 1：手動指定 resp.encoding
resp.encoding = "utf-8"  # 亦可使用 resp.apparent_encoding
soup_fix1 = BeautifulSoup(resp.text, "html.parser")
price_fix1 = soup_fix1.select_one(".price_color").text
print(f"[修法1] 價格 = {price_fix1}")

# 4. 修法 2：直接使用二進位 resp.content (由 BeautifulSoup 自動辨識或自行 decode)
soup_fix2 = BeautifulSoup(resp.content, "html.parser")
price_fix2 = soup_fix2.select_one(".price_color").text
print(f"[修法2] 價格 = {price_fix2}")
