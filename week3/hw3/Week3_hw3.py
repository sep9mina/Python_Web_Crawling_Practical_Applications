import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

print("=== 開始執行爬蟲程式 ===")

base_url = "https://www.scrapethissite.com/pages/forms/"
target_teams = ["Los Angeles Kings", "Detroit Red Wings"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

all_rows = []

for team in target_teams:
    print(f"\n[1] 正在查詢隊伍：{team}")
    page = 1
    
    while True:
        params = {"q": team, "page_num": page}
        try:
            print(f"    --> 正在抓取第 {page} 頁資料...")
            response = requests.get(base_url, headers=headers, params=params, timeout=15)
            response.raise_for_status()
        except Exception as e:
            print(f"    [連線錯誤]：{e}")
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", class_="table")
        
        if not table:
            print("    找不到資料表格，結束該隊伍搜尋。")
            break

        rows = table.find_all("tr", class_="team")
        if not rows:
            print("    該頁已無隊伍資料。")
            break

        print(f"    成功獲取 {len(rows)} 筆資料！")

        for row in rows:
            name = row.find("td", class_="name").get_text(strip=True) if row.find("td", class_="name") else ""
            year = row.find("td", class_="year").get_text(strip=True) if row.find("td", class_="year") else ""
            wins = row.find("td", class_="wins").get_text(strip=True) if row.find("td", class_="wins") else ""
            losses = row.find("td", class_="losses").get_text(strip=True) if row.find("td", class_="losses") else ""
            ot_losses = row.find("td", class_="ot-losses").get_text(strip=True) if row.find("td", class_="ot-losses") else ""
            pct = row.find("td", class_="pct").get_text(strip=True) if row.find("td", class_="pct") else ""
            gf = row.find("td", class_="gf").get_text(strip=True) if row.find("td", class_="gf") else ""
            ga = row.find("td", class_="ga").get_text(strip=True) if row.find("td", class_="ga") else ""
            diff = row.find("td", class_="diff").get_text(strip=True) if row.find("td", class_="diff") else ""

            # 嚴格篩選只留下目標隊名
            if name in target_teams:
                all_rows.append({
                    "Team Name": name,
                    "Year": year,
                    "Wins": wins,
                    "Losses": losses,
                    "OT Losses": ot_losses,
                    "Win %": pct,
                    "Goals For (GF)": gf,
                    "Goals Against (GA)": ga,
                    "+ / -": diff
                })

        # 判斷是否有下一頁分頁按鈕
        pagination = soup.find("ul", class_="pagination")
        if pagination and pagination.find("a", {"aria-label": "Next"}):
            page += 1
            time.sleep(0.5)
        else:
            break

# 匯出資料至 Excel
if all_rows:
    df = pd.DataFrame(all_rows)
    output_path = "output.xlsx"
    df.to_excel(output_path, index=False, engine="openpyxl")
    print(f"\n==========================================")
    print(f"[成功完成] 共擷取 {len(df)} 筆資料！")
    print(f"檔案已儲存為：{output_path}")
    print(f"==========================================")
else:
    print("\n[警告] 未能擷取到任何符合的隊伍資料，請檢查網路連線。")
