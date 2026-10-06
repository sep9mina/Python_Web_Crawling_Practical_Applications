import pandas as pd
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

print("-" * 10 + " Response (伺服器回應內容) " + "-" * 10)
print(f"[Response] 狀態碼={resp.status_code} {resp.reason}")
print(f"[Response] Content-Type={resp.headers.get('Content-Type')}")
print(f"[Response] 編碼={resp.encoding}")
print(f"[Response] 花費秒數={resp.elapsed.total_seconds():.2f}")
print(f"[Response] User-Agent={resp.request.headers['User-Agent']}")
print("-" * 40)

# ==========================================
# Step 2：取得且解析網頁原始碼
# ==========================================
soup = BeautifulSoup(resp.text, "html.parser")

# 每個國家卡片都位於 class 為 "col-md-4 country" 的 div 內
country_divs = soup.find_all("div", class_="country")

taiwan_info = None

for div in country_divs:
    # 提取國家名稱（位於 <h3> 標籤內）
    name_tag = div.find("h3", class_="country-name")
    country_name = name_tag.get_text(strip=True) if name_tag else ""

    # 比對是否為 Taiwan
    if country_name == "Taiwan":
        capital = div.find("span", class_="country-capital").get_text(strip=True)
        population = div.find("span", class_="country-population").get_text(strip=True)
        area = div.find("span", class_="country-area").get_text(strip=True)

        taiwan_info = {
            "Country": country_name,
            "Capital": capital,
            "Population": population,
            "Area (km²)": area,
        }
        break

print("[Step 2 擷取結果]:", taiwan_info)

# ==========================================
# Step 3：轉換網頁表格成 DataFrame 清單
# ==========================================
if taiwan_info:
    # 建立 DataFrame（單筆資料放入 list 轉為表格列）
    df = pd.DataFrame([taiwan_info])
    print("\n[Step 3 DataFrame]:")
    print(df)

    # ==========================================
    # Step 4：DataFrame 寫入 Excel
    # ==========================================
    output_file = "taiwan_data.xlsx"
    df.to_excel(output_file, index=False)
    print(f"\n[Step 4] 成功匯出至 {output_file}")
else:
    print("未找到 Taiwan 的相關資料。")
