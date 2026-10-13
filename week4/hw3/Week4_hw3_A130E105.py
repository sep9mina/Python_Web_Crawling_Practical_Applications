import csv
import os
import requests
from bs4 import BeautifulSoup

# 1. 自動取得本程式檔案所在的資料夾，確保 CSV 永遠儲存在同一目錄
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, "hockey_teams.csv")

# 2. 目標網站（第一頁）
url = "https://www.scrapethissite.com/pages/forms/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

print("正在發送請求至目標網站...")
response = requests.get(url, headers=headers)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

# 3. 9個欄位名稱
headers_csv = [
    "team_name",
    "year",
    "wins",
    "losses",
    "ot_losses",
    "win_pct",
    "goals_for",
    "goals_against",
    "diff",
]

data_rows = []

# 4. 使用 select 系列方法選取所有球隊資料列（class 為 team 的 tr）
rows = soup.select("table.table tr.team")

for row in rows:
    # 使用 select_one 選取各別欄位
    name_el = row.select_one("td.name")
    year_el = row.select_one("td.year")
    wins_el = row.select_one("td.wins")
    losses_el = row.select_one("td.losses")
    ot_losses_el = row.select_one("td.ot-losses")
    pct_el = row.select_one("td.pct")
    gf_el = row.select_one("td.gf")
    ga_el = row.select_one("td.ga")
    diff_el = row.select_one("td.diff")

    # 提取文字並去除頭尾空白字元
    team_name = name_el.get_text(strip=True) if name_el else ""
    year = year_el.get_text(strip=True) if year_el else ""
    wins = wins_el.get_text(strip=True) if wins_el else ""
    losses = losses_el.get_text(strip=True) if losses_el else ""
    ot_losses = ot_losses_el.get_text(strip=True) if ot_losses_el else ""
    win_pct = pct_el.get_text(strip=True) if pct_el else ""
    goals_for = gf_el.get_text(strip=True) if gf_el else ""
    goals_against = ga_el.get_text(strip=True) if ga_el else ""
    diff = diff_el.get_text(strip=True) if diff_el else ""

    data_rows.append(
        [
            team_name,
            year,
            wins,
            losses,
            ot_losses,
            win_pct,
            goals_for,
            goals_against,
            diff,
        ]
    )

# 5. 寫入 CSV 檔案（使用 utf-8-sig 確保 Excel 開啟不亂碼）
with open(csv_file_path, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(headers_csv)
    writer.writerows(data_rows)

print(f"成功儲存 {len(data_rows)} 筆資料至：{csv_file_path}")
