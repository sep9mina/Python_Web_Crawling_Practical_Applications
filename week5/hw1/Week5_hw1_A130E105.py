import csv
import os
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

# 取得目前執行的 .py 檔所在資料夾路徑，並組合輸出檔名
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "authors.csv")

base_url = "http://quotes.toscrape.com/"
response = requests.get(base_url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

quote_blocks = soup.find_all("div", class_="quote")
data_list = []

for block in quote_blocks:
  quote_text = block.find("span", class_="text").get_text(strip=True)
  author_name = block.find("small", class_="author").get_text(strip=True)

  tag_elements = block.find_all("a", class_="tag")
  tags = ";".join([tag.get_text(strip=True) for tag in tag_elements])

  about_link = block.find("a", href=True)
  born_date = ""
  born_location = ""

  if about_link and "about" in about_link.get_text().lower():
    author_url = urljoin(base_url, about_link["href"])
    res_author = requests.get(author_url)
    res_author.encoding = "utf-8"
    author_soup = BeautifulSoup(res_author.text, "html.parser")

    date_elem = author_soup.find("span", class_="author-born-date")
    location_elem = author_soup.find("span", class_="author-born-location")

    if date_elem:
      born_date = date_elem.get_text(strip=True)
    if location_elem:
      born_location = location_elem.get_text(strip=True)

  data_list.append({
      "name": author_name,
      "born_date": born_date,
      "born_location": born_location,
      "quote": quote_text,
      "tags": tags,
  })

headers = ["name", "born_date", "born_location", "quote", "tags"]

# 使用組合好的絕對路徑寫入檔案
with open(csv_path, mode="w", newline="", encoding="utf-8-sig") as csv_file:
  writer = csv.DictWriter(csv_file, fieldnames=headers)
  writer.writeheader()
  writer.writerows(data_list)

print(f"爬取完成，已成功儲存至：{csv_path}")
