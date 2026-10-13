import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

# 選取所有書名連結 <a>（位於 <h3> 內）
books = soup.select("h3 > a")

# 取出前 5 本書進行比對輸出
for book in books[:5]:
    text_title = book.text.strip()          # 畫面顯示文字
    full_title = book.get("title", "")     # 標籤內的完整 title 屬性
    print(f"{text_title} → {full_title}")
