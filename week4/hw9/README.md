<img width="1477" height="690" alt="image" src="https://github.com/user-attachments/assets/64b4f347-947b-45ed-86a2-4fcc0f04c020" />

## 1. HTTP 網路請求與偽裝（requests）
#### GET 請求：使用 requests.get() 向目標網站發送 HTTP 請求並取得 HTML 原始碼。
#### 請求標頭設定（Headers / User-Agent）：自訂瀏覽器標頭，避免請求被目標網站視為惡意機器人或被反爬蟲機制阻擋。
#### 編碼設定：指定 utf-8 編碼，確保解析中文字元或特殊符號時不會出現亂碼。

## 2. DOM 樹解析與 CSS 選擇器（BeautifulSoup4）
#### HTML 解析：利用 html.parser 將靜態 HTML 字串轉換為可操作的樹狀結構（DOM Tree）。
#### 階層式 CSS 選擇器（select）：
#### 使用 .side_categories ul li ul li a 精確定位第二層分類，過濾掉最外層無效的「Books」總分類。
#### 使用 article.product_pod h3 a 精確鎖定各商品卡片的書名節點。

## 3. HTML 屬性與文字擷取技巧
#### 完整資訊提取（HTML 屬性 vs. 標籤文字）：
#### 書名文字若過長會在前端被截斷（帶有 ...），程式透過 book.get("title") 讀取 title 屬性中的未截斷完整名稱。
#### 字串清理：使用 get_text(strip=True) 自動去除文字前後的多餘空格與換行符號。

## 4. 網址動態組合與路徑解析（urllib.parse.urljoin）
#### 相對路徑轉絕對路徑：爬取到的 href 通常是相對路徑（例如 catalogue/category/...），利用標準庫的 urljoin() 自動結合基礎網址（Base URL），生成可用於發送下一次請求的完整 URL。

## 5. 兩階段跳轉爬取（Two-Step / Multi-level Crawling）
#### 階層式爬蟲邏輯：
#### 第一階段（首頁）：獲取所有分類清單與連結。
#### 第二階段（分類子頁）：鎖定特定目標（Travel 分類連結），發起二次請求進入分類內頁爬取特定清單。

## 6. 資料結構化與 CSV 匯出（csv）
#### 結構化存檔：使用 csv.DictWriter 以字典格式寫入資料，自動對應欄位名稱（category、url）。
#### 編碼相容性（utf-8-sig）：在輸出 CSV 時使用 utf-8-sig（帶 BOM），避免在 Windows / Excel 開啟 CSV 檔案時產生亂碼。



<img width="1177" height="960" alt="image" src="https://github.com/user-attachments/assets/117427a4-6282-4f7a-bb0c-af2bbbc6ce43" />

<img width="1037" height="1027" alt="image" src="https://github.com/user-attachments/assets/d64287a1-dd9f-4bc6-b563-a02cd4e221f4" />
