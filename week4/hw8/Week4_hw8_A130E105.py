import requests
from bs4 import BeautifulSoup
from collections import Counter

url = "https://books.toscrape.com/"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

# -------------------------------------------------------------
# 任務 1：統計首頁 20 本書各星等的數量
# HTML 結構中星星標籤為：<p class="star-rating Three">
# 概念：「class 也可以是資料」，從 class list 中取出星等名稱
# -------------------------------------------------------------
star_ratings = []
for p in soup.select("article.product_pod p.star-rating"):
    # classes 會是例如 ['star-rating', 'Three']
    # 取出排除 'star-rating' 之後的那個 class 名稱
    rating = [c for c in p["class"] if c != "star-rating"][0]
    star_ratings.append(rating)

# 依特定順序統計
order = ['One', 'Two', 'Three', 'Four', 'Five']
counts = Counter(star_ratings)
rating_summary = {k: counts.get(k, 0) for k in order}

print(f"各星等數量 : {rating_summary} 合計 {len(star_ratings)} 本\n")

# -------------------------------------------------------------
# 任務 2：用一行 selector 列出所有五星書的完整書名
# 核心技巧：
# 1. CSS Selector 同時選取具備 .star-rating 與 .Five 的節點之同層/下層連結，
#    直接定位：article.product_pod:has(p.star-rating.Five) h3 a 
#    或標準 CSS 兄弟選取器：p.star-rating.Five + h3 a
# 2. 完整書名存在於 <a> 標籤的 'title' 屬性中（若取 .text 會遇到省略符號 "..."）
# -------------------------------------------------------------
five_star_books = [a["title"] for a in soup.select("article.product_pod:has(p.star-rating.Five) h3 a")]

print(f"五星書共 {len(five_star_books)} 本 :")
for title in five_star_books:
    print(f" - {title}")
