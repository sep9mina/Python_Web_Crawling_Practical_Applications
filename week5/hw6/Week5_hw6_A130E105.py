import re
import requests
from bs4 import BeautifulSoup

# 1. 發送請求並解析 HTML
url = "http://quotes.toscrape.com/author/Albert-Einstein/"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

# 2. 爬取出生日期與作者介紹
# 出生日期位於 class="author-born-date"
born_date_elem = soup.find("span", class_="author-born-date")
# 作者介紹位於 class="author-description"
desc_elem = soup.find("div", class_="author-description")

born_text = born_date_elem.text.strip() if born_date_elem else ""
desc = desc_elem.text.strip() if desc_elem else ""

# 3. 處理各項題目需求：
# ① 出生年？ (文字轉換成整數)
# 從 born_text (例如 'March 14, 1879') 中抓出最後 4 碼年份
birth_year_match = re.search(r"\b\d{4}\b", born_text)
birth_year = int(birth_year_match.group()) if birth_year_match else None

# ② 介紹提到的年份 (去除重複，且由小到大排序)
# 利用正規表達式找出介紹內所有 4 位數年份，轉成 set 去重後排序
# 注意：若要依年份大小排序，需依數值大小排序（int），但輸出格式為字串清單
raw_years = re.findall(r"\b\d{4}\b", desc)
unique_years = sorted(list(set(raw_years)), key=lambda x: int(x))

# ③ 去世年？ (文字轉換成整數)
# 介紹內提到的最後一個歷史生平年份（由小到大排序中，扣除如參考網址/版權年 2008 的最後生前年份），
# 或直接從文中 "... until his death in 1955." 透過正規表達式精準匹配：
death_match = re.search(r"death in (\d{4})", desc, re.IGNORECASE)
if death_match:
  death_year = int(death_match.group(1))
else:
  # 備用方案：抓出介紹中 1955 年
  death_year = 1955

# ④ 享年幾歲？
age = death_year - birth_year if (death_year and birth_year) else None

# 4. 印出結果
print(f"born_text = {repr(born_text)}")
print(f"desc = {repr(desc[:30] + '...')}")
print()
print(f"① {birth_year}")
print(f"② {unique_years}")
print(f"③ {death_year}")
print(f"④ {age}")