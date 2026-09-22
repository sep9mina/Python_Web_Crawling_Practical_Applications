import os
import time
from io import StringIO
import pandas as pd
import requests

BASE_URL = "https://www.scrapethissite.com/pages/forms/"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

all_dfs = []
TOTAL_PAGES = 24

print("開始爬取所有分頁資料...")

# 使用 Session 維持連線，減少被伺服器斷線的機率
with requests.Session() as session:
    session.headers.update(HEADERS)

    for page in range(1, TOTAL_PAGES + 1):
        params = {"page_num": page}
        success = False
        max_retries = 3  # 每頁最多重試 3 次

        for attempt in range(max_retries):
            try:
                resp = session.get(BASE_URL, params=params, timeout=20)
                resp.raise_for_status()

                # 解析網頁表格
                tables = pd.read_html(StringIO(resp.text))
                if tables:
                    df_page = tables[0]
                    all_dfs.append(df_page)
                    print(
                        f"第 {page}/{TOTAL_PAGES} 頁抓取成功（共"
                        f" {len(df_page)} 筆）"
                    )

                success = True
                break  # 成功抓取就跳出重試迴圈

            except requests.RequestException as e:
                print(
                    f"第 {page} 頁第 {attempt + 1} 次抓取失敗（{e}），等待"
                    " 3 秒後重試..."
                )
                time.sleep(3)

        if not success:
            print(f"❌ 第 {page} 頁重試多次後仍失敗，略過此頁。")

        # 稍微拉長間隔至 1 秒
        time.sleep(1)

# 合併所有表格並輸出
if all_dfs:
    final_df = pd.concat(all_dfs, ignore_index=True)
    print(f"\n全部爬取完成！總共有 {len(final_df)} 筆隊伍資料。")

    output_path = os.path.join(
        os.path.dirname(__file__), "hockey_teams_full.xlsx"
    )
    final_df.to_excel(output_path, index=False)
    print(f"檔案已儲存至：{output_path}")
else:
    print("未抓取到任何資料。")
