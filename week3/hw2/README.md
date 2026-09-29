<img width="1675" height="794" alt="image" src="https://github.com/user-attachments/assets/febcecca-1480-48c0-a483-f03668632d2b" />

## 自動爬取冰球隊伍統計網頁的搜尋結果，將資料儲存為 CSV 試算表，並完整記錄網路連線與處理流程的日誌（log）。   
#### 1.連線與日誌記錄：利用 Python 內建的 logging 模組，完整記錄連線除錯細節（包含毫秒時間戳記與底層 urllib3 連線資訊）。 
#### 2.網頁資料抓取：對目標網站發出 HTTP GET 請求，取得包含搜尋條件 q=boston 的網頁 HTML 內容。
#### 3.HTML 解析與萃取：利用 BeautifulSoup 定位目標表格，自動提取表格欄位標題與每一列冰球隊伍的統計數值。
#### 4.輸出結構化檔案：將萃取出的資料轉成 pandas 的 DataFrame，最後匯出成 output.csv 供 Excel 開啟，並在 w03.log 記錄最終處理筆數與儲存路徑。  

<img width="707" height="746" alt="image" src="https://github.com/user-attachments/assets/fc5426d6-8f10-45fa-a860-f11c6c69aaea" />

## 配置日誌系統（Logging Setup）
#### 設定記錄檔名為 w03.log。
#### 定義記錄格式（包含日期時間、毫秒、層級、模組名稱與訊息內容）。 
#### 開啟 urllib3 的 DEBUG 記錄層級，藉此記錄 HTTPS 底層連線的握手與狀態。 

## 發送請求並記錄狀態（HTTP Request）
#### 定義目標網址為 [https://www.scrapethissite.com/pages/forms/?q=boston&per_page=25](https://www.scrapethissite.com/pages/forms/?q=boston&per_page=25)。 
#### 加上瀏覽器標頭（User-Agent）模擬正常使用者訪問。使用 requests.get() 發送網路請求，並在日誌記錄伺服器回傳的 HTTP 狀態碼（如 200）。   

<img width="1086" height="960" alt="image" src="https://github.com/user-attachments/assets/86a526c1-8fc3-4d84-9254-e54098c6585f" />

## 解析網頁資料（HTML Parsing）
#### 使用 BeautifulSoup 載入網頁原始碼並解析 DOM 結構。
#### 抓取 <th> 標籤以取得所有欄位名稱（如 Team Name, Year, Wins...）。 
#### 逐列遍歷 <tr class="team"> 標籤，讀取每個儲存格 <td> 的文字內容並清理前後空白。
#### 組裝成 pandas 的二維表格物件（DataFrame），並在日誌輸出抓到的資料筆數與欄數（如「取得 21 筆 x 9 欄」）。 

## 輸出檔案與存檔確認（File Export）
#### 呼叫 df.to_csv("output.csv") 存檔，設定 utf-8-sig 編碼避免中文在 Excel 中開啟亂碼。
#### 取得檔案的絕對路徑，寫入最後一條記錄訊息至 w03.log（例如「已存檔：D:...」）。

<img width="1230" height="156" alt="image" src="https://github.com/user-attachments/assets/53d1e23d-d385-46b2-845e-04072b115caf" />

<img width="702" height="499" alt="image" src="https://github.com/user-attachments/assets/b6f85da0-fa98-4a98-85e4-4496ebc3f7ae" />
