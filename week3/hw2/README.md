<img width="698" height="497" alt="image" src="https://github.com/user-attachments/assets/8d6b6c4c-8307-40d2-9ad3-f08fe788ff63" /><img width="1675" height="794" alt="image" src="https://github.com/user-attachments/assets/febcecca-1480-48c0-a483-f03668632d2b" />

## 自動爬取冰球隊伍統計網頁的搜尋結果，將資料儲存為 CSV 試算表，並完整記錄網路連線與處理流程的日誌（log）。   
##### 1.連線與日誌記錄：利用 Python 內建的 logging 模組，完整記錄連線除錯細節（包含毫秒時間戳記與底層 urllib3 連線資訊）。 
##### 2.網頁資料抓取：對目標網站發出 HTTP GET 請求，取得包含搜尋條件 q=boston 的網頁 HTML 內容。
##### 3.HTML 解析與萃取：利用 BeautifulSoup 定位目標表格，自動提取表格欄位標題與每一列冰球隊伍的統計數值。
##### 4.輸出結構化檔案：將萃取出的資料轉成 pandas 的 DataFrame，最後匯出成 output.csv 供 Excel 開啟，並在 w03.log 記錄最終處理筆數與儲存路徑。  

<img width="707" height="746" alt="image" src="https://github.com/user-attachments/assets/fc5426d6-8f10-45fa-a860-f11c6c69aaea" />

<img width="1086" height="960" alt="image" src="https://github.com/user-attachments/assets/86a526c1-8fc3-4d84-9254-e54098c6585f" />

<img width="1230" height="156" alt="image" src="https://github.com/user-attachments/assets/53d1e23d-d385-46b2-845e-04072b115caf" />

<img width="702" height="499" alt="image" src="https://github.com/user-attachments/assets/b6f85da0-fa98-4a98-85e4-4496ebc3f7ae" />
