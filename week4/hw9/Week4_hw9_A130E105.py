import csv
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"

# 設定請求標頭
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}

# 1. 請求首頁
response = requests.get(BASE_URL, headers=headers)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

# 2. 爬取左側書籍分類清單
# 側邊欄分類選單位於 class 為 'side_categories' 底下的 <ul> 內部
categories_list = soup.select(".side_categories ul li ul li a")

categories_data = []
travel_url = None

for a_tag in categories_list:
    category_name = a_tag.get_text(strip=True)
    relative_url = a_tag.get("href")
    full_url = urljoin(BASE_URL, relative_url)

    categories_data.append({"category": category_name, "url": full_url})

    if category_name.lower() == "travel":
        travel_url = full_url

# 3. 儲存成 categories.csv
csv_filename = "categories.csv"
with open(csv_filename, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["category", "url"])
    writer.writeheader()
    writer.writerows(categories_data)

print(f"共 {len(categories_data)} 個分類，已存檔：{csv_filename}\n")

# 4. 進入 Travel 分類爬取所有書名
if travel_url:
    travel_res = requests.get(travel_url, headers=headers)
    travel_res.encoding = "utf-8"
    travel_soup = BeautifulSoup(travel_res.text, "html.parser")

    # 書名位於 <h3> 標籤下的 <a> 標籤中
    # 注意：a 標籤中的文字可能會被截斷，完整書名儲存在 'title' 屬性中
    book_tags = travel_soup.select("article.product_pod h3 a")

    travel_books = []
    for book in book_tags:
        # 優先抓取 title 屬性，若沒有則抓文字
        book_title = book.get("title") or book.get_text(strip=True)
        travel_books.append(book_title)

    print(f"Travel 分類共 {len(travel_books)} 本書：")
    for title in travel_books:
        print(f"- {title}")
