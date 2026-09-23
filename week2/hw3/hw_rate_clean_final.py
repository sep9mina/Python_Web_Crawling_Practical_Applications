import time
import pandas as pd
from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL = "https://rate.bot.com.tw/xrt?Lang=zh-TW"

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
print("正在開啟頁面...")
driver.get(URL)

print("等待驗證與頁面載入...")
time.sleep(8)

table = driver.find_element(By.TAG_NAME, "table")
table_html = table.get_attribute("outerHTML")
driver.quit()

dfs = pd.read_html(StringIO(table_html))
raw = dfs[0]

# 攤平多層欄位標題
raw.columns = ["_".join([str(c) for c in col if "Unnamed" not in str(c)]) for col in raw.columns]

# 去掉整欄都是空的
raw = raw.dropna(axis=1, how="all")

# 去掉內容完全重複的欄位（RWD 重複輸出）
raw = raw.loc[:, ~raw.T.duplicated()]

# 明確去掉「查詢」連結欄（遠期匯率查詢按鈕那欄）
raw = raw.drop(columns=[c for c in raw.columns if raw[c].astype(str).eq("查詢").any()])

# 明確只留一欄幣別（幣別相關欄位可能因空白字元沒被判定為重複）
name_cols = [c for c in raw.columns if "幣別" in c]
if len(name_cols) > 1:
    raw = raw.drop(columns=name_cols[1:])

print("最終欄位：", raw.columns.tolist(), "共", raw.shape[1], "欄")
print(raw.head())

output_file = "20260922.xlsx"
raw.to_excel(output_file, index=False)
print(f"已輸出：{output_file}")
