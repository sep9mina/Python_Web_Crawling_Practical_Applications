import os
from io import StringIO
import pandas as pd
import requests

# 1. 目標網址與 Request Headers 設定
URL = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

print("正在發送請求至臺灣銀行...")
resp = requests.get(URL, headers=HEADERS, timeout=20)
resp.raise_for_status()

# 2. 解析網頁中的表格
tables = pd.read_html(StringIO(resp.text))
raw_df = tables[0]

# 3. 處理多層表頭與欄位選取
# 取前 5 欄：幣別、現金買入、現金賣出、即期買入、即期賣出
clean_df = raw_df.iloc[:, :5].copy()

clean_df.columns = [
    "幣別",
    "現金匯率_本行買入",
    "現金匯率_本行賣出",
    "即期匯率_本行買入",
    "即期匯率_本行賣出",
]

# 4. 清理幣別文字雜訊（例如去除行動版重複出現的文字）
clean_df["幣別"] = clean_df["幣別"].str.extract(r"([^\x00-\x7F]+\s*\([A-Z]+\))")

print("匯率資料整理完成，預覽前 5 筆：")
print(clean_df.head())

# 5. 儲存為 Excel 檔案
output_file = "20260922.xlsx"
output_path = os.path.join(os.path.dirname(__file__), output_file)
clean_df.to_excel(output_path, index=False)

print(f"\n已成功輸出乾淨的 Excel 檔案：{output_path}")
