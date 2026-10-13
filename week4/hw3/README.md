<img width="1580" height="787" alt="image" src="https://github.com/user-attachments/assets/15fa483b-401b-4a42-a203-387a06b496d8" />

<img width="955" height="171" alt="image" src="https://github.com/user-attachments/assets/747fadf4-6b92-4248-ad5e-6293bd0dca48" />

## 技術
#### requests 模組：
##### 負責模擬瀏覽器發送 HTTP GET 請求，向目標伺服器取得靜態 HTML 網頁原始碼。
##### 搭配 User-Agent 標頭避免被基礎反爬機制阻擋，並設定 utf-8 編碼防止文字亂碼。

#### BeautifulSoup4（HTML 解析器）：

##### 將網頁原始碼轉換為樹狀結構（DOM Tree）。

##### 使用 CSS 選擇器語法（.select() 與 .select_one()）進行節點定位。

#### os 模組（絕對路徑處理）：

##### 利用 os.path.abspath(__file__) 取得目前執行中的 .py 腳本真實路徑。

##### 避免終端機因工作目錄（Working Directory）不同而將檔案存錯位置（例如跑到 C 槽）。

#### csv 模組：

##### 負責結構化資料的儲存，採用 utf-8-sig 編碼寫入，確保 Excel 開啟時不會產生亂碼。

<img width="772" height="610" alt="image" src="https://github.com/user-attachments/assets/22a38e98-6867-4926-888a-fa5b30d447ac" />
