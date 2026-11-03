<img width="1581" height="639" alt="image" src="https://github.com/user-attachments/assets/8b59c14e-dd50-4cca-8e2c-834778f81eb3" />
## 使用 Session 登入並爬取存成 CSV
#### Quotes to Scrape 登入時會包含一個隱藏的 csrf_token 表單欄位，必須先 GET 取得 token 後再 POST 送出登入資料。

## 會話維持機制、動態防禦欄位擷取、HTML 結構定位與清理，以及防亂碼的 CSV 匯出處理。

## 1. requests.Session() 連線狀態與 Cookie 維持
#### 技術痛點：一般的 requests.get() 或 requests.post() 彼此獨立（Stateless），發送第二次請求時，伺服器發給你的登入憑據（Session Cookie）就會丟失。
#### 技術作法：使用 with requests.Session() as session: 建立會話物件。它會在底層自動接收伺服器回傳的 Set-Cookie，並在後續每一次發送請求（例如從登入頁切換到首頁）時自動帶上 Cookie，確保爬蟲在目標網站始終維持「已登入」的身分。

## 2. 處理 CSRF Token（跨站請求偽造防護）
#### 技術痛點：許多網站（包括此題的登入表單）為防禦惡意外部腳本直接 POST 帳號密碼，會在 HTML 裡埋設隨機生成的隱藏欄位 <input type="hidden" name="csrf_token" value="...">。如果直接 POST 帳密而未帶 Token，伺服器會直接拒絕（回傳 400 或 403）。
#### 技術作法：先發送一次 session.get(LOGIN_URL) 取得登入頁原始 HTML。使用 BeautifulSoup 找到該隱藏標籤並取出屬性值：Pythoncsrf_token = soup_login.find("input", {"name": "csrf_token"})["value"]
#### 將取出的動態 Token 連同帳號、密碼包進 payload 字典中，再發送 session.post() 完成合法的身分驗證。


## 4. BeautifulSoup 節點解析與標籤串接
#### 區塊化遍歷：先定位每一條名言的父節點 find_all("div", class_="quote")，再從各個區塊內部使用 find() 縮小搜尋範圍抓取文字與作者，避免資料欄位對齊錯位。
#### 多筆資料合併（List Comprehension + join）：Pythontag_elements = block.find_all("a", class_="tag")
#### tags = ";".join([tag.get_text(strip=True) for tag in tag_elements])此處使用列表推導式取出多個標籤文字並用 strip=True 去除空白換行，再透過 ";".join() 組合成單一字串，符合資料庫或 CSV 欄位的單元格式。

## 5. csv.DictWriter 與 utf-8-sig 編碼
#### 結構化寫入：採用 csv.DictWriter 搭配事先定義好的欄位名稱 ["page", "quote", "author", "tags"]，讓每筆資料以字典型態寫入（writer.writerows(quotes_data)），欄位順序固定且不容易因缺少欄位而產生位移。
#### Excel 防亂碼編碼：檔案開啟時指定 encoding="utf-8-sig"，會自動在 CSV 檔頭寫入 UTF-8 的 BOM（Byte Order Mark）。這樣日後用微軟 Excel 直接點開檢視名言或作者字串時，不會出現中文或特殊符號亂碼。

<img width="658" height="829" alt="image" src="https://github.com/user-attachments/assets/07de209c-f6f4-4535-b601-3ed203d7754e" />

<img width="657" height="174" alt="image" src="https://github.com/user-attachments/assets/5842030d-43cd-4780-9721-7074451b55df" />

![Uploading image.png…]()

