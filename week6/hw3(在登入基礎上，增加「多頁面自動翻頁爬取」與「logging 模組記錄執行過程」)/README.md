<img width="1597" height="639" alt="image" src="https://github.com/user-attachments/assets/8938cbb2-f257-4794-8b4d-3a9403204203" />
## logging 日誌記錄配置
### 使用 logging.basicConfig() 統一格式化時間與層級訊息（%(asctime)s [%(levelname)s] %(message)s）。
### 透過 handlers 同時配置：
#### logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")：將日誌完整存入指定的 week_06_ex3_Quotes_login.log 檔案。
#### logging.StreamHandler()：同步即時印在終端機，方便執行時確認進度。
#### 每一頁解析出 quote_blocks 後，即時以 logging.info() 記錄「第 X 頁爬取完成，共抓取到 Y 句名言」。

## 自動翻頁機制（while 迴圈搭配 Next 按鈕）
### 不寫死頁數（例如固定跑 10 頁），而是透過 BeautifulSoup 尋找底部的 <li class="next"><a href="...">。
### 取出下一頁的相對路徑後，用 requests.compat.urljoin(BASE_URL, next_href) 自動組裝成完整網址，當找不到下一頁按鈕時將 current_url 設為 None 自動跳出迴圈。

## 維持 Session 進行分頁抓取
### 全程保持在 with requests.Session() as session: 區塊內，讓翻頁時的每次 GET 請求都能維持已登入狀態。

## CSV 寫入設定   欄位指定為 ["page", "quote", "author", "tags"]。   採用 utf-8-sig 編碼儲存至 quotes_all.csv，避免中文或特殊引號在 Excel 開啟時出現亂碼。   

<img width="661" height="778" alt="image" src="https://github.com/user-attachments/assets/61e4bb12-9521-48e0-898c-b24ad9fb7851" />
<img width="739" height="751" alt="image" src="https://github.com/user-attachments/assets/94ffaace-12e0-4eb3-9084-468ea40d40a6" />
<img width="719" height="495" alt="image" src="https://github.com/user-attachments/assets/8ac8f8ee-cba0-4c8a-8120-a38db40e2f12" />
<img width="789" height="452" alt="image" src="https://github.com/user-attachments/assets/96682709-f69a-4a72-9e66-5bac01f9d1d2" />
<img width="1525" height="791" alt="image" src="https://github.com/user-attachments/assets/a7bce69e-ce52-4d63-a94a-0e48197fd2d9" />
