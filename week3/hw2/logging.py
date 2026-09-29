import os
import logging
import requests
from bs4 import BeautifulSoup
import pandas as pd

# ---------------------------------------------------------
# 1. 設定日誌 (Logging)
# ---------------------------------------------------------
log_filename = "w03.log"

# 設定 logging 格式與記錄等級（包含毫秒格式）
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s,%(msecs)03d [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_filename, mode="w", encoding="utf-8"),
        logging.StreamHandler()  # 同時印在螢幕上方便除錯
    ]
)

# 依圖片需求，urllib3 需要輸出連線 DEBUG 訊息
logging.getLogger("urllib3").setLevel(logging.DEBUG)
logger = logging.getLogger("w03")

# ---------------------------------------------------------
# 2. 發送請求爬取網頁
# ---------------------------------------------------------
# 觀察 log 截圖，目標 URL 帶有搜尋參數 q=boston&per_page=25
url = "https://www.scrapethissite.com/pages/forms/?q=boston&per_page=25"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(url, headers=headers)
logger.info(f"狀態碼={response.status_code}，網址={url}")

# ---------------------------------------------------------
# 3. 解析 HTML 表格
# ---------------------------------------------------------
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", class_="table")

# 取得表頭標題
headers_list = [th.text.strip() for th in table.find_all("th")]

# 取得每一列資料
rows = []
for tr in table.find_all("tr", class_="team"):
    cols = [td.text.strip() for td in tr.find_all("td")]
    if cols:
        rows.append(cols)

# 建立 DataFrame
df = pd.DataFrame(rows, columns=headers_list)
logger.info(f"取得 {len(df)} 筆 x {len(headers_list)} 欄")

# ---------------------------------------------------------
# 4. 存成 CSV 檔（同時產生截圖顯示的 output.csv）
# ---------------------------------------------------------
output_csv = "output.csv"
df.to_csv(output_csv, index=False, encoding="utf-8-sig")

# 輸出儲存路徑資訊至 log（模擬截圖最後一行）
abs_path = os.path.abspath(output_csv)
logger.info(f"已存檔：{abs_path}")

print("\n完成！已產出 output.csv 與 w03.log。")
