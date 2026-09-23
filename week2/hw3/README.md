## 課堂練習３
## 爬取臺灣銀行本日營業時間牌告匯率
#### 將本日牌告費率存成 20260922.xlsx 檔
#### URL | https://rate.bot.com.tw/xrt?Lang=zh TW

## 爬取會遇到的問題點
##### 臺灣銀行的網頁表格有「雙層表頭（多層級欄位，MultiIndex）」與合併儲存格：
##### 上層是大標題：「幣別」、「現金匯率」、「即期匯率」。
##### 下層是細項：現金匯率底下又拆成「本行買入」、「本行賣出」；即期匯率也拆成「本行買入」、「本行賣出」。
##### 幣別欄位甚至還混雜了「幣別名稱（如 美金 USD）」與行動版重複文字。
##### 如果直接使用最簡單的 pd.read_html 抓下來，欄位會變成多重層級（Tuple 結構），存進 Excel 或查看時容易錯亂。

## 程式碼關鍵處理方式
##### 1.處理雙層表頭：重新命名為清晰乾淨的單層欄位（幣別、現金買入、現金賣出、即期買入、即期賣出）。
##### 2.清洗幣別字串：剔除網頁標籤帶有的多餘空白與英文重複字。

## 安裝套件
##### lxml 與 openpyxl：pip install lxml openpyxl
##### pandas 及相關套件：pip install requests pandas openpyxl lxml

##### 臺灣銀行的 HTML 表格結構較為複雜（包含巢狀標籤與合併格），pandas.read_html() 在使用 lxml 解析失敗時，會自動嘗試切換到容錯率更高的 html5lib 與 beautifulsoup4 解析器。
##### 網頁解析套件：pip install html5lib beautifulsoup4

## 報錯與排除
##### 1.ValueError: No tables found 代表 pandas 在抓回來的 HTML 中找不到 <table> 標籤。
##### 臺灣銀行網站近期加強了防爬蟲機制，若沒有加上完整的瀏覽器標頭（特別是 Accept-Language 等），伺服器回應的內容會是一段被重定向或阻擋的空白提示頁面，而不是原本的匯率頁面。
##### 解決方式：補齊 Headers，改用 BeautifulSoup 精準鎖定表格
##### 將請求標頭補齊為完整瀏覽器規格，並透過 beautifulsoup4（bs4）直接抓取匯率表格。
##### 以上還是爬不到資料

### 加幾行 debug，先確認電腦實際收到的內容
##### print("狀態碼:", resp.status_code)
##### print("內容長度:", len(resp.text))
##### print("內容預覽:")
##### print(resp.text)

<img width="710" height="315" alt="image" src="https://github.com/user-attachments/assets/d86bac53-71c2-4b64-b31c-9af57382419e" />

##### Challenge Validation 是臺銀網站的機器人驗證機制（類似 reCAPTCHA 的技術，這裡用的是加密運算挑戰），它偵測到 requests 送出的請求「不是真的瀏覽器」，就攔截下來丟出這個驗證頁面，不管加多完整的 headers 都沒用——因為它連瀏覽器的 JavaScript 執行環境、TLS 指紋這些都會檢查，單純的 requests 套件模擬不出來。

## 改測試爬官方CSV下載連結

<img width="700" height="116" alt="image" src="https://github.com/user-attachments/assets/e4049b64-f056-43a7-9edf-e77b6554b64c" />

##### CSV 端點也被同一層驗證擋下來了，確定這個網站現在對所有非瀏覽器請求都會擋。

##改用能真的執行 JavaScript、通過驗證的工具 Selenium 開一個真實 Chrome 瀏覽器去載入頁面。
##### 安裝套件：pip install selenium
##### Selenium 4 之後會自動抓對應版本的 ChromeDriver，不用手動下載，但電腦上要有安裝 Google Chrome 瀏覽器。

## chrome目前受到自動軟體測試軟體控制
<img width="958" height="504" alt="image" src="https://github.com/user-attachments/assets/0c1acc01-53e8-49cf-93f7-2e0dd4519c25" />


