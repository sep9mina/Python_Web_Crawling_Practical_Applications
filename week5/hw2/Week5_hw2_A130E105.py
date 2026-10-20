import csv
from datetime import datetime
from collections import Counter
from pathlib import Path
import requests
from bs4 import BeautifulSoup

# 設定基礎網址與輸出檔案路徑（儲存在當前 Python 檔案相同目錄下）
BASE_URL = "http://quotes.toscrape.com"
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "authors.csv"

# 1. 取得首頁 HTML
response = requests.get(BASE_URL)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

quotes_elements = soup.find_all("div", class_="quote")

data_list = []
author_details_cache = {}  # 快取作者個人資料，避免重複請求相同頁面

for q in quotes_elements:
    # 提取名言並去除頭尾引號
    raw_quote = q.find("span", class_="text").get_text()
    clean_quote = raw_quote.strip("“”\"' ")

    # 提取標籤
    tag_elements = q.find_all("a", class_="tag")
    tags = ", ".join([t.get_text() for t in tag_elements])

    # 提取作者名稱與個人簡介連結
    author_name = q.find("small", class_="author").get_text().strip()
    author_link = q.find("a", href=True, text="(about)")["href"]

    # 進入作者頁面取得生日與出生地
    if author_name not in author_details_cache:
        author_res = requests.get(BASE_URL + author_link)
        author_soup = BeautifulSoup(author_res.text, "html.parser")
        born_date = author_soup.find("span", class_="author-born-date").get_text().strip()
        born_loc = author_soup.find("span", class_="author-born-location").get_text().strip()
        author_details_cache[author_name] = {
            "born_date": born_date,
            "born_location": born_loc,
        }

    born_info = author_details_cache[author_name]

    data_list.append({
        "name": author_name,
        "born_date": born_info["born_date"],
        "born_location": born_info["born_location"],
        "quote": clean_quote,
        "tags": tags,
    })

# 2. 存成 authors.csv 到程式碼所在目錄
csv_headers = ["name", "born_date", "born_location", "quote", "tags"]
with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=csv_headers)
    writer.writeheader()
    writer.writerows(data_list)

print(f"authors.csv 已成功儲存至：{OUTPUT_FILE}\n")

# 3. 統計與問題解答（針對首頁的不重複作者）
unique_authors = list(author_details_cache.items())

# (1) 統計各國有幾位作者
countries = []
for name, info in unique_authors:
    loc = info["born_location"]
    # 格式通常為 "in City, Country" 或 "in Country"
    country = loc.replace("in ", "").split(",")[-1].strip()
    countries.append(country)

country_counts = Counter(countries)

print("各國作者人數統計：")
for country, count in country_counts.items():
    print(f" - {country}: {count} 位")

# (2) 誰最早出生？
earliest_author = None
earliest_date = None

for name, info in unique_authors:
    try:
        parsed_date = datetime.strptime(info["born_date"], "%B %d, %Y")
    except ValueError:
        parsed_date = datetime.strptime(info["born_date"], "%b %d, %Y")

    if earliest_date is None or parsed_date < earliest_date:
        earliest_date = parsed_date
        earliest_author = (name, info["born_date"], info["born_location"])

print(f"\n 最早出生的作者是：{earliest_author[0]}")
print(f"   出生日期：{earliest_author[1]}")
print(f"   出生地點：{earliest_author[2]}")