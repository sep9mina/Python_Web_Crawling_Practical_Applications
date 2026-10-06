import requests
from bs4 import BeautifulSoup

# ==========================================
# Step 1：解析伺服器回應的 Response
# ==========================================
URL = "https://www.scrapethissite.com/pages/simple/"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    )
}

resp = requests.get(URL, headers=HEADERS, timeout=10)

# ==========================================
# 課堂練習 1：設定 CSS Selectors 並驗證
# ==========================================
SELECTORS = {
    "國家卡片": ".country",
    "國名": ".country-name",
    "首都": ".country-capital",
    "人口": ".country-population",
    "面積": ".country-area",
}

# 解析網頁原始碼
soup = BeautifulSoup(resp.text, "html.parser")

# 自動檢查：驗證每個欄位是否都抓到 250 筆
for name, selector in SELECTORS.items():
    elements = soup.select(selector)
    count = len(elements)
    if count == 250:
        print(f"[OK] {name:<6} {selector:<20} 抓到 {count} 筆")
    else:
        print(f"[XX] {name:<6} {selector:<20} 抓到 {count} 筆 (需為 250 筆)")
