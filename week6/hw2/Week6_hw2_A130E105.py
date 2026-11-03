import csv
import requests
from bs4 import BeautifulSoup

LOGIN_URL = "http://quotes.toscrape.com/login"
BASE_URL = "http://quotes.toscrape.com"
OUTPUT_FILE = "quotes_first_page.csv"

# 建立 Session 維持連線狀態（保留 Cookie）
with requests.Session() as session:
    # 1. 先進入登入頁面抓取 csrf_token
    res_login_page = session.get(LOGIN_URL)
    soup_login = BeautifulSoup(res_login_page.text, "html.parser")
    csrf_token = soup_login.find("input", {"name": "csrf_token"})["value"]

    # 2. 準備表單資料並發送 POST 登入請求（此練習網站帳密可任意輸入）
    payload = {
        "csrf_token": csrf_token,
        "username": "testuser",
        "password": "password123",
    }
    session.post(LOGIN_URL, data=payload)

    # 3. 登入後抓取第一頁的名言
    res_quotes = session.get(BASE_URL)
    soup_quotes = BeautifulSoup(res_quotes.text, "html.parser")

    quotes_data = []
    quote_blocks = soup_quotes.find_all("div", class_="quote")

    for block in quote_blocks:
        # 取得名言文字（去掉前後引號）
        text = block.find("span", class_="text").get_text(strip=True)
        # 取得作者
        author = block.find("small", class_="author").get_text(strip=True)
        # 取得所有標籤，並以分號 (;) 串接
        tag_elements = block.find_all("a", class_="tag")
        tags = ";".join([tag.get_text(strip=True) for tag in tag_elements])

        quotes_data.append(
            {"page": 1, "quote": text, "author": author, "tags": tags}
        )

# 4. 存成 quotes_first_page.csv
fieldnames = ["page", "quote", "author", "tags"]
with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(quotes_data)

print(f"成功爬取 {len(quotes_data)} 筆名言，已存成 {OUTPUT_FILE}")