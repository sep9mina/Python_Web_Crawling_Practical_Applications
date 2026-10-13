import requests
from bs4 import BeautifulSoup
import pandas as pd

# ==========================================
# 網路請求與防護繞過 (HTTP Requests)
# - 使用 requests 發送 GET 請求取得目標 HTML
# - 加入自訂 User-Agent 模擬真實瀏覽器行為，避免連線遭拒
# ==========================================
url = "https://scrapethissite.com/pages/simple/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"


# ==========================================
# HTML DOM 解析與節點走訪 (Web Scraping / BeautifulSoup)
# - 建立 BeautifulSoup 物件解析 HTML 樹狀結構
# - 使用 find_all / find 依 CSS class 批次定位目標節點並取出純文字
# ==========================================
soup = BeautifulSoup(response.text, "html.parser")

# 找出所有包含國家資訊的父容器 (class="country")
country_divs = soup.find_all("div", class_="country")

data = []

for country in country_divs:
    # 依指定 class 擷取對應子標籤的純文字資訊
    name_tag = country.find("h3", class_="country-name")
    capital_tag = country.find("span", class_="country-capital")
    pop_tag = country.find("span", class_="country-population")
    area_tag = country.find("span", class_="country-area")

    name = name_tag.get_text(strip=True) if name_tag else ""
    capital = capital_tag.get_text(strip=True) if capital_tag else ""
    pop_str = pop_tag.get_text(strip=True) if pop_tag else "0"
    area_str = area_tag.get_text(strip=True) if area_tag else "0"

    # ==========================================
    # 資料清洗與數值型態轉換 (Data Cleaning)
    # - 移除千分位逗號與非數值雜訊
    # - 將文字轉型為 int 與 float，利於後續數值運算與排序
    # - 搭配 try-except 進行異常處理，避免資料缺漏中斷程式
    # ==========================================
    try:
        population = int(pop_str.replace(",", ""))
    except ValueError:
        population = 0

    try:
        area_km2 = float(area_str.replace(",", ""))
    except ValueError:
        area_km2 = 0.0

    data.append({
        "name": name,
        "capital": capital,
        "population": population,
        "area_km2": area_km2,
    })


# ==========================================
# 資料分析、排序與檔案輸出 (Data Analysis & Export / Pandas)
# - 將結構化資料載入 DataFrame
# - 匯出為 countries.csv（採用 utf-8-sig 防止 Excel 開啟亂碼）
# - 使用 sort_values 與 head(5) 篩選前五名並格式化輸出
# ==========================================
df = pd.DataFrame(data)

# 1. 輸出至 CSV 檔案
df.to_csv("countries.csv", index=False, encoding="utf-8-sig")
print("成功爬取並儲存 countries.csv！共", len(df), "筆資料。")

# 2. 統計分析：人口數前五大國家
print("\n=== 人口數前五大國家 ===")
top_5_population = df.sort_values(by="population", ascending=False).head(5)
for idx, row in top_5_population.reset_index(drop=True).iterrows():
    print(f"{idx + 1}. {row['name']} - 人口: {row['population']:,}")

# 3. 統計分析：國土面積前五大國家
print("\n=== 國土面積前五大國家 ===")
top_5_area = df.sort_values(by="area_km2", ascending=False).head(5)
for idx, row in top_5_area.reset_index(drop=True).iterrows():
    print(f"{idx + 1}. {row['name']} - 面積: {row['area_km2']:,.1f} km²")
