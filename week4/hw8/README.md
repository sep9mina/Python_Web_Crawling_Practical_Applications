<img width="1439" height="718" alt="image" src="https://github.com/user-attachments/assets/f00e9f34-4042-433b-b8aa-3bdd717ed81a" />

## 運用靜態網頁爬蟲技巧進行資料定位、屬性抽取與統計
## HTTP 請求與編碼處理 (requests)
#### 利用 requests.get() 發送 HTTP GET 請求取得目標網站的原始 HTML 文本。
#### 設定 response.encoding = 'utf-8' 確保文字內容編碼正確、避免中文或特殊字元亂碼。

## Class 作為資料（Class as Data）的屬性解析概念
#### 非文字型資料抽取：評分資訊並非放在一般標籤文本（.text）內，而是以 CSS 類別的形式呈現（例如 <p class="star-rating Three">）。
#### 屬性剖析：透過 BeautifulSoup 讀取標籤屬性 tag["class"]（取得類別清單），並透過清單過濾或列表推導式，將代表星等的 Class 名稱（如 One、Three、Five）轉化為可分析的資料。

## 高階 CSS Selector 定位與條件篩選 (soup.select())
#### 複合/相鄰選取器：運用進階 CSS 選擇器精準定位條件，例如利用相鄰兄弟選取器（p.star-rating.Five + h3 a）或結構虛擬類別（:has()），達到一行 Selector 就精確鎖定「五星評分卡片內的書名連結」。
#### 隱藏/完整屬性取值：針對網頁上文字被截斷（有 ...）的狀況，精準定位並抓取 <a> 標籤內的 title 屬性（a["title"]），而非直接讀取 .text，以取得最完整的原始書名。

## 資料聚合與統計分類 (collections.Counter / 字典映射)
#### 將解析出的類別資料（星等字串）進行頻率統計。
#### 透過字典依據固定順序（One 到 Five）輸出標準化統計格式，計算各星等數量與總合。

<img width="959" height="997" alt="image" src="https://github.com/user-attachments/assets/b1403eb2-1369-4e14-92c8-fdadeffd0075" />






