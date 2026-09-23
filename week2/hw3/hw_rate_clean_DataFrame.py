import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL = "https://rate.bot.com.tw/xrt?Lang=zh-TW"

options = Options()
options.add_argument("--start-maximized")
# 先不要用 headless，讓妳看得到瀏覽器實際發生什麼事，方便除錯

driver = webdriver.Chrome(options=options)

print("正在開啟頁面...")
driver.get(URL)

print("等待驗證與頁面載入...")
time.sleep(8)  # 給 Challenge Validation 一點時間跑完，之後可依實際狀況調整秒數

# 確認表格是否出現
try:
    table = driver.find_element(By.TAG_NAME, "table")
    print("成功找到表格！")
except Exception as e:
    print("還是沒找到表格：", e)
    driver.quit()
    raise

# 取出表格 HTML，交給 pandas 解析
table_html = table.get_attribute("outerHTML")
dfs = pd.read_html(table_html)
df = dfs[0]

print(df.head())

driver.quit()

output_file = "20260922.xlsx"
df.to_excel(output_file, index=False)
print(f"已輸出：{output_file}")
