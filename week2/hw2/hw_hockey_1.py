import os
from io import StringIO
import pandas as pd
import requests

# 1. 設定目標網址與模擬瀏覽器的 User-Agent 標頭
URL = "https://www.scrapethissite.com/pages/forms/"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# 2. 發送 GET 請求取得網頁內容
resp = requests.get(URL, headers=HEADERS, timeout=20)
resp.raise_for_status()  # 若狀態碼非 200 會主動拋出例外
print(f"網頁請求成功，狀態碼：{resp.status_code}")

# 3. 使用 pandas 解析 HTML 裡面的所有 <table> 表格
html_str = resp.text
tables = pd.read_html(StringIO(html_str))

# 取出網頁中的第一個表格
df = tables[0]

# 4. 設定輸出路徑並儲存為 hockey_teams.xlsx
output_path = os.path.join(os.path.dirname(__file__), "hockey_teams.xlsx")
df.to_excel(output_path, index=False)

print(f"成功儲存！檔案路徑：{output_path}")
