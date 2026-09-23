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


