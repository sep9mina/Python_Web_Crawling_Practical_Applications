<img width="1481" height="768" alt="image" src="https://github.com/user-attachments/assets/8597aef6-8cba-4058-81df-9d4595482ff8" />

<img width="947" height="411" alt="image" src="https://github.com/user-attachments/assets/20d3d279-aed6-4886-97d6-7ef53584a107" />

## 網路請求與防護繞過（HTTP Requests）
##### 使用 requests 套件發送 GET 請求取得目標網頁的原始 HTML 內容，並加入自訂 headers（User-Agent）模擬真實瀏覽器行為，避免伺服器因爬蟲特徵而阻擋連線。

## HTML DOM 解析與節點走訪（Web Scraping / BeautifulSoup）
##### 利用 BeautifulSoup 的 find 與 find_all 系列方法，依據 CSS class（如 .country、.country-name 等）鎖定目標節點，精準批次萃取特定標籤內的純文字資訊（get_text(strip=True)）。

## 資料清洗與數值型態轉換（Data Cleaning）
##### 針對擷取出的非結構化文字，去除空白字元與千分位逗號，並將字串轉換為對應的數值型別（整數 int 與浮點數 float），同時利用例外處理（try-except）確保缺漏值或格式異常時程式能穩健執行。

## 資料分析、排序與檔案輸出（Data Analysis & Export / Pandas）
##### 將清洗後的結構化字典列表轉換為 pandas.DataFrame，運用 sort_values 搭配 head(5) 進行遞減排序與 Top 5 篩選，最後以 utf-8-sig 編碼輸出為 .csv 檔案，確保在 Excel 等工具開啟時不會產生中文或特殊字元亂碼。  

<img width="1044" height="1018" alt="image" src="https://github.com/user-attachments/assets/4d3bc1d5-768c-49e9-86d2-eba3abdc07fc" />
