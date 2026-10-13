<img width="1490" height="717" alt="image" src="https://github.com/user-attachments/assets/c0b0ce1f-7f1a-4abf-a5f6-54c5d033da80" />

## 網路爬蟲中的文字編碼識別與亂碼處理機制

## 1. HTTP 回應標頭解析與預設編碼判斷 (resp.headers & resp.encoding)
#### 原理：爬蟲透過 requests.get() 取得回應時，requests 會優先檢查 HTTP Header 中的 Content-Type 是否帶有字元集（如 charset=utf-8）。
#### 亂碼成因：當伺服器僅回傳 text/html 而未宣告 charset 時，requests 會遵循 RFC 規範預設採用 ISO-8859-1（Latin-1） 來解碼，導致原本是多位元組的 UTF-8 特殊符號（如英鎊 £，Hex 為 C2 A3）被拆解成單位元組顯示為 Â£。

## 2. 內容特徵自動編碼偵測 (resp.apparent_encoding)
#### 原理：利用底層的字元編碼偵測套件（如 charset_normalizer 或 chardet），直接分析 HTML 原始二進位位元組流（bytes）的統計特徵與內容規則，推算出該網頁極可能採用的真實編碼（即 utf-8）。

## 3. 字串層級手動重新指定編碼 (resp.encoding)
#### 原理：在呼叫 resp.text 之前，手動覆寫 resp.encoding = 'utf-8' 或 resp.encoding = resp.apparent_encoding。
#### 效果：強制 resp.text 屬性在將底層 bytes 轉換為 Python 字串時，以正確的字元集進行解碼（Decode），避免讀取階段產生亂碼。

## 4. 二進位資料傳遞與 DOM 解析器自動偵測 (resp.content)
#### 原理：不經由 requests 轉譯為字串，直接提取原始二進位資料 resp.content 傳入 BeautifulSoup(resp.content, 'html.parser')。
#### 效果：交由 BeautifulSoup 內建的編碼嗅探機制（檢查 HTML <meta charset="..."> 標籤）自動識別並正確解碼 HTML 樹狀結構，從根源繞過 requests 預設解碼的干擾。

<img width="921" height="815" alt="image" src="https://github.com/user-attachments/assets/00a78c77-9f0f-47f8-a055-86b19085f815" />
