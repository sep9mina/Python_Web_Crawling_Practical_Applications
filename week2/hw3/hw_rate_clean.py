import os
from bs4 import BeautifulSoup
import pandas as pd
import requests

URL = "https://rate.bot.com.tw/xrt?Lang=zh-TW"

# 設定更完整的瀏覽器標頭，避免被臺銀伺服器擋下
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
}

print("正在發送請求至臺灣銀行...")
resp = requests.get(URL, headers=HEADERS, timeout=20)
resp.raise_for_status()

# 透過 BeautifulSoup 解析網頁
soup = BeautifulSoup(resp.text, "html.parser")
table = soup.find("table")

if not table:
    raise ValueError(
        "仍未找到表格，請確認連線狀態或網頁內容是否被阻擋！"
    )

# 取出表格所有列
data = []
rows = table.find("tbody").find_all("tr")

for row in rows:
    # 1. 抓取幣別（只抓取中文與英文代碼區塊）
    currency_div = row.find(
        "div", class_="visible-phone print_full-inline"
    ) or row.find("div", class_="print_show")
    if currency_div:
        currency = currency_div.get_text(strip=True)
    else:
        currency = row.find("td").get_text(strip=True)

    # 2. 抓取匯率數值（前 4 個數值格剛好對應 現金買入/賣出、即期買入/賣出）
    rate_cells = row.find_all(
        "td", class_="rate-content-cash text-right print_table-cell"
    ) + row.find_all(
        "td", class_="rate-content-sight text-right print_table-cell"
    )

    cash_buy = rate_cells[0].get_text(strip=True) if len(rate_cells) > 0 else "-"
    cash_sell = (
        rate_cells[1].get_text(strip=True) if len(rate_cells) > 1 else "-"
    )
    sight_buy = (
        rate_cells[2].get_text(strip=True) if len(rate_cells) > 2 else "-"
    )
    sight_sell = (
        rate_cells[3].get_text(strip=True) if len(rate_cells) > 3 else "-"
    )

    data.append(
        {
            "幣別": currency,
            "現金匯率_本行買入": cash_buy,
            "現金匯率_本行賣出": cash_sell,
            "即期匯率_本行買入": sight_buy,
            "即期匯率_本行賣出": sight_sell,
        }
    )

clean_df = pd.DataFrame(data)

print("匯率資料整理完成，預覽前 5 筆：")
print(clean_df.head())

# 儲存為 Excel 檔案
output_file = "20260922.xlsx"
output_path = os.path.join(os.path.dirname(__file__), output_file)
clean_df.to_excel(output_path, index=False)

print(f"\n已成功輸出乾淨的 Excel 檔案：{output_path}")
