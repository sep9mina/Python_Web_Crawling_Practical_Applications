import csv
import urllib.parse
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.scrapethissite.com"
MAIN_URL = f"{BASE_URL}/pages/frames/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}

# 1. 抓取主頁面並尋找 iframe 的 src 網址
print("正在讀取主頁面...")
main_res = requests.get(MAIN_URL, headers=headers)
main_soup = BeautifulSoup(main_res.text, "html.parser")

iframe = main_soup.select_one("iframe#iframe, iframe")
if not iframe or not iframe.get("src"):
    print("找不到 iframe 元素！")
    exit()

# 組合 iframe 的完整真實網址
iframe_url = urllib.parse.urljoin(MAIN_URL, iframe["src"])
print(f"找到 iframe 真實網址: {iframe_url}")

# 2. 進入 iframe 頁面抓取所有烏龜卡片
frame_res = requests.get(iframe_url, headers=headers)
frame_soup = BeautifulSoup(frame_res.text, "html.parser")

# 尋找卡片（使用 select 系列）
cards = frame_soup.select(".turtle-family-card, .turtle-family, .col-md-4")
# 若上述抓到太多雜項，做進一步篩選（包含 family 名稱的卡片）
cards = [c for c in cards if c.select_one(".family-name, h3")]

print(f"找到卡片數量: {len(cards)}")

turtle_data = []

for card in cards:
    # 抓取科名 (family)
    family_elem = card.select_one(".family-name, h3")
    family = family_elem.text.strip() if family_elem else ""

    # 抓取 Learn more 按鈕連結
    btn = card.select_one("a.button, a.btn, a")
    detail_url = ""
    if btn and btn.get("href"):
        detail_url = urllib.parse.urljoin(iframe_url, btn["href"])

    common_name = ""
    discovered_year = ""
    discovered_by = ""
    image_url = ""

    # 進入詳細資料頁面
    if detail_url:
        d_res = requests.get(detail_url, headers=headers)
        d_soup = BeautifulSoup(d_res.text, "html.parser")

        c_name = d_soup.select_one(".common-name")
        d_year = d_soup.select_one(".discovered-year")
        d_by = d_soup.select_one(".discovered-by")
        img = d_soup.select_one(".turtle-image, img.img-responsive, img")

        common_name = c_name.text.strip() if c_name else ""
        discovered_year = d_year.text.strip() if d_year else ""
        discovered_by = d_by.text.strip() if d_by else ""

        if img and img.get("src"):
            image_url = urllib.parse.urljoin(detail_url, img["src"])

    turtle_data.append(
        {
            "family": family,
            "common_name": common_name,
            "discovered_year": discovered_year,
            "discovered_by": discovered_by,
            "image_url": image_url,
        }
    )

    print(f"成功擷取: {family} - {common_name}")

print(f"\n總共抓取 {len(turtle_data)} 筆，準備寫入 turtles.csv...")

# 3. 寫入 CSV 檔案
fieldnames = [
    "family",
    "common_name",
    "discovered_year",
    "discovered_by",
    "image_url",
]
with open("turtles.csv", mode="w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(turtle_data)

print("寫入完成！現在可以打開 turtles.csv 查看了。")
