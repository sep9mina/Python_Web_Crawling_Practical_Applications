import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = "https://rate.bot.com.tw/xrt?Lang=zh-TW"

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
print("正在開啟頁面...")
driver.get(URL)

print("等待驗證與頁面載入...")
time.sleep(8)

# 拿通過驗證之後、瀏覽器實際渲染出來的完整 HTML
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")
table = soup.find("table")

if not table:
    raise ValueError("還是沒找到表格，把 html 存檔起來檢查。")

data = []
rows = table.find("tbody").find_all("tr")

for row in rows:
    currency_div = row.find("div", class_="visible-phone print_show") \
        or row.find("div", class_="print_show")
    if currency_div:
        currency = currency_div.get_text(strip=True)
    else:
        currency = row.find("td").get_text(strip=True)

    rate_cells = row.find_all("td", class_="rate-content-cash") + \
                 row.find_all("td", class_="rate-content-sight")

    def get_text(cells, i):
        return cells[i].get_text(strip=True) if len(cells) > i else "-"

    data.append({
        "幣別": currency,
        "現金匯率_本行買入": get_text(rate_cells, 0),
        "現金匯率_本行賣出": get_text(rate_cells, 1),
        "即期匯率_本行買入": get_text(rate_cells, 2),
        "即期匯率_本行賣出": get_text(rate_cells, 3),
    })

df = pd.DataFrame(data)
print(df.head())

output_file = "20260922.xlsx"
df.to_excel(output_file, index=False)
print(f"已輸出：{output_file}")
