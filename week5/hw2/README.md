<img width="1571" height="673" alt="image" src="https://github.com/user-attachments/assets/90e32655-47f7-486f-b914-171ecaefc24c" />

<img width="637" height="718" alt="image" src="https://github.com/user-attachments/assets/4dbcf4a2-a631-4bde-b81b-e2f362bc45e8" />
<img width="804" height="888" alt="image" src="https://github.com/user-attachments/assets/b8b7a5f4-1d37-42f1-8afe-d041c71ad6c9" />
<img width="1136" height="817" alt="image" src="https://github.com/user-attachments/assets/9e44c9e5-dc60-4a1a-a7bb-d3e129d752be" />


## 技術：網路爬蟲、字串與資料清洗、資料結構與統計分析

## 二層網頁巡訪與爬取（Two-Level Crawling）

#### ● 首頁卡片僅包含作者姓名與語錄，出生的年月日與地點需點擊 (about) 連結至作者詳情頁。
#### ● 透過解析首頁的相對路徑 href，拼接完整網址（BASE_URL + author_link）發起第二層請求取得深度資料。

## 快取機制與請求最佳化（Request Caching）
#### ● 首頁多則語錄常出自同一位作者（如 Albert Einstein）。
#### ● 建立字典（author_details_cache）暫存已抓取過的作者資訊，避免對相同頁面重複發出 HTTP 請求，能顯著提升執行速度並減輕目標伺服器負擔。

## 文字清理與符號去除（Data Cleaning）
#### ● 使用 .strip('“”"\' ') 精確過濾語錄頭尾的直引號、彎引號與多餘空白，同時保留語錄內部可能存在的對話引號。
#### ● 出生地點字串（如 "in Ulm, Germany"）透過 .replace("in ", "").split(",")[-1].strip() 擷取最後逗號後的國域名稱。

## 時間解析與比較（Datetime Parsing）
#### ● 利用 datetime.strptime() 將英文日期字串（%B %d, %Y 或 %b %d, %Y）轉為標準時間物件，藉由時間戳進行數值比較，精準找出最早出生的作者。

## 資料彙整與匯出（Data Structuring & Export）
#### ● 運用 collections.Counter 快速統計各國作者人數分布。
#### ● 使用 Python 內建 csv.DictWriter 將整理後的欄位資料（name、born_date、born_location、quote、tags）結構化寫入 CSV 檔案，並以 utf-8-sig 編碼避免在 Excel 中開啟時出現亂碼。

<img width="1747" height="495" alt="image" src="https://github.com/user-attachments/assets/98b82aa7-a30d-43ec-ae8b-be9cd01442a9" />
