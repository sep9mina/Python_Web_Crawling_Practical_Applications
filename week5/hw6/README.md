<img width="1578" height="795" alt="image" src="https://github.com/user-attachments/assets/91d709fc-919e-409f-a46d-74c2e7332ccc" />
<img width="655" height="633" alt="image" src="https://github.com/user-attachments/assets/2bd27230-31a3-401b-8dd9-ba23fd4a5b4b" />
<img width="819" height="515" alt="image" src="https://github.com/user-attachments/assets/15ea58b3-5f59-4ee2-84b3-803fa27533aa" />
<img width="857" height="237" alt="image" src="https://github.com/user-attachments/assets/97133841-1682-4f1a-b54c-9a6dfd30f287" />

## 1. HTTP 請求與編碼處理 (requests)
#### ● 網路請求發送：使用 requests.get() 取得目標網頁的原始 HTML 文本。
#### ● 字元編碼設定：指定 response.encoding = "utf-8"，確保網頁文字在讀取與後續解析時不會產生亂碼。

## 2. DOM 樹解析與定位 (BeautifulSoup)
#### ● HTML解析器：透過 BeautifulSoup(..., "html.parser") 將 HTML 字串轉為可查詢的節點物件。
#### ● 特定標籤提取：使用 soup.find() 搭配 CSS 類別（如 class_="author-born-date" 與 class_="author-description"），精準定位目標區塊，並利用 .text.strip() 萃取純文字並去除頭尾空白字元。

## 3. 正規表達式文字萃取 (re)
#### ● 特定格式提取：使用 \b\d{4}\b 邊界與4 位數模式比對，自非結構化的文字中抓出符合年份特徵的數字串。
#### ● 語境關鍵字捕獲：運用捕獲群組語法（如 re.search(r"death in (\d{4})", ...)），避免單純抓取最大數字時誤判非生平年份（例如引用出處的版權年份 2008），實現高準確度的條件提取。

## 4. 資料清洗、去重與自訂排序
#### ● 資料結構去重：利用 set() 資料結構消除同一文字段落中重複提及的年份。
#### ● 數值型鍵值排序：使用 sorted(..., key=lambda x: int(x))，避免字串預設的字典序排序問題，確保年份清單維持嚴格的「由小到大」數字順序。
#### ● 型別轉換與運算：將萃取出的文字格式數字轉型為整數（int），進行基本的數值運算（享年計算：去世年 - 出生年）。
