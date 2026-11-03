import csv
import logging
import requests
from bs4 import BeautifulSoup

LOGIN_URL = "http://quotes.toscrape.com/login"
BASE_URL = "http://quotes.toscrape.com"
CSV_FILE = "quotes_all.csv"
LOG_FILE = "week_06_ex3_Quotes_login.log"

# 1. 設定 logging 模組
# 同時輸出到檔案（LOG_FILE）與終端機畫面
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

all_quotes = []

with requests.Session() as session:
    # 2. 登入流程：取得 csrf_token 並發送 POST
    logging.info("開始連線登入頁面...")
    res_login_page = session.get(LOGIN_URL)
    soup_login = BeautifulSoup(res_login_page.text, "html.parser")
    csrf_token = soup_login.find("input", {"name": "csrf_token"})["value"]

    payload = {
        "csrf_token": csrf_token,
        "username": "testuser",
        "password": "password123",
    }
    session.post(LOGIN_URL, data=payload)
    logging.info("登入請求已送出，開始爬取名言資料...")

    # 3. 逐頁爬取流程
    current_url = BASE_URL
    page_num = 1

    while current_url:
        logging.info(f"正在爬取第 {page_num} 頁：{current_url}")
        res = session.get(current_url)
        soup = BeautifulSoup(res.text, "html.parser")

        quote_blocks = soup.find_all("div", class_="quote")
        page_quote_count = len(quote_blocks)

        # 記錄該頁抓取到的名言數量
        logging.info(f"第 {page_num} 頁爬取完成，共抓取到 {page_quote_count} 句名言")

        for block in quote_blocks:
            text = block.find("span", class_="text").get_text(strip=True)
            author = block.find("small", class_="author").get_text(strip=True)
            tag_elements = block.find_all("a", class_="tag")
            tags = ";".join([tag.get_text(strip=True) for tag in tag_elements])

            all_quotes.append(
                {"page": page_num, "quote": text, "author": author, "tags": tags}
            )

        # 4. 判斷是否有下一頁（找尋 li.next > a）
        next_btn = soup.find("li", class_="next")
        if next_btn and next_btn.find("a"):
            next_href = next_btn.find("a")["href"]
            current_url = requests.compat.urljoin(BASE_URL, next_href)
            page_num += 1
        else:
            logging.info("已到達最後一頁，爬取結束。")
            current_url = None

# 5. 將所有資料寫入 quotes_all.csv
fieldnames = ["page", "quote", "author", "tags"]
with open(CSV_FILE, mode="w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_quotes)

logging.info(f"所有名言已成功儲存至 {CSV_FILE}，總計 {len(all_quotes)} 筆資料。")