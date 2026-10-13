<img width="1485" height="677" alt="image" src="https://github.com/user-attachments/assets/96f929f2-bfbd-4377-9b84-5fde0ad8a297" />

## 技術：
### iframe 跨層網頁解析與反爬繞過
#### 原理：目標網站主頁面使用 HTML <iframe> 標籤嵌入資料。若直接向主頁面發送請求，只能取得空框架。
#### 應用：分析出框架內部的真實來源網址（?frame=true）並直接對其發送請求，繞過 iframe 的載入限制以順利抓取卡片資料。

### BeautifulSoup CSS 選擇器（select / select_one）
#### 原理：利用 CSS 選擇器語法（如標籤、class、巢狀結構）精確定位 DOM 節點。
#### 應用：使用 soup.select("div.turtle-family-card") 批次定位 14 種烏龜項目，並使用 select_one() 抓取子節點中的各項欄位值（如 h3.family-name、span.common-name、img.turtle-image 等）。

### 雙層深度爬蟲（Multi-level Web Scraping）與 URL 拼接
#### 原理：第一層列表頁僅提供部分摘要，更詳細的欄位需點擊進入子頁面。
#### 應用：程式先在列表層抓取「Learn more →」按鈕的相對連結，透過 urllib.parse.urljoin() 組裝成完整 URL，再發送二次請求進入詳細頁面擷取發現者、年份與圖片等欄位。 

### 結構化資料匯出與 CSV 編碼處理（UTF-8 with BOM）
#### 原理：將非結構化的網頁文本整理成字典陣列，並標準化匯出至試算表檔案。
#### 應用：使用 Python 內建 csv.DictWriter 對應指定的欄位名稱依序寫入；同時指定 encoding="utf-8-sig"（加入 BOM 檔頭），解決 Windows 與 Excel 開啟 CSV 時常發生的亂碼問題。   

<img width="997" height="910" alt="image" src="https://github.com/user-attachments/assets/af893a3c-9548-4857-91d5-a2aeb1ae34e0" />

<img width="1488" height="368" alt="image" src="https://github.com/user-attachments/assets/34b00fb1-3a8a-4a04-be31-93c1dc4a890a" />


## debug：
#### 上一版程式碼，FRAME_URL 設成了 ?frame=true，但伺服器回傳的依舊是「最外層的包裹頁面」（包含 <iframe id="iframe" ...>），所以直接用卡片的 class 找會找不到。
#### 解決方式：先向 [https://www.scrapethissite.com/pages/frames/](https://www.scrapethissite.com/pages/frames/) 請求。
#### 使用 BeautifulSoup 的 select_one("#iframe") 抓出 src 屬性。
#### 再向該 src 的網址請求，就能順利抓到裡面的烏龜與卡片！
