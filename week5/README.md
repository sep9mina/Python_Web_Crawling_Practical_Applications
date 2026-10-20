<img width="1589" height="689" alt="image" src="https://github.com/user-attachments/assets/406cba0e-6603-45f5-9fdf-d81d0aa9602c" />

<img width="897" height="978" alt="image" src="https://github.com/user-attachments/assets/089a9d4a-65f8-49d8-8b9c-4f0ed4c52390" />
<img width="871" height="583" alt="image" src="https://github.com/user-attachments/assets/2098ced5-3713-4161-82d3-524789d25406" />



## 1. 二段式深度爬取（Two-Step Crawling）
#### ● 層級化資料獲取：首頁卡片僅包含名言文字、作者姓名與標籤；作者的出生日期與出生地則存放在獨立頁面。程式透過解析首頁 (about) 超連結，進一步對作者個人頁面發送二次請求，達成跨頁面的關聯資料整合。   

#### ● 相對路徑拼接：使用 urllib.parse.urljoin 將 HTML 屬性中的相對路徑（如 /author/Albert-Einstein）動態組合為完整的 HTTP 請求網址，確保請求合法有效。

## 2. DOM 解析與元素定位（BeautifulSoup）
#### ● 區塊拆解：使用 soup.find_all("div", class_="quote") 將首頁劃分為獨立的名言卡片單元，確保每筆資料的欄位精準對齊。
#### ● 階層過濾與文字清理：
#### ▲ 使用 .get_text(strip=True) 去除 HTML 標籤內部的多餘空白與換行符號。
#### ▲ 運用串列生成式（List Comprehension）搭配 ";".join(...)，將單一卡片內的複數標籤元素扁平化合併為單一字串。
#### ▲ 透過條件判斷式（if elem:）確保若目標元素缺失時程式不會因 NoneType 報錯中斷（防呆機制）。

## 3. 跨工作目錄的動態路徑鎖定（os 模組）
#### ● 解除終端機執行目錄限制：利用 os.path.abspath(__file__) 取得當前執行腳本的實體路徑，並透過 os.path.dirname() 抓取其所在資料夾。
#### ● 可攜式檔案路徑：使用 os.path.join() 拼接輸出路徑，保證無論使用者在命令列的哪個目錄（如 C:\Users\owner）啟動程式，產出的檔案都會固定寫入腳本同層目錄（如 d:\A130E105\Python_Web_Crawling\）。

## 4. 結構化資料輸出與 Excel 相容處理（csv 模組）
#### ● 字典寫入器（csv.DictWriter）：將每筆抓取到的資料以鍵值對（Key-Value）形式收集至串列中，透過 fieldnames 定義明確的欄位順序（name、born_date、born_location、quote、tags），並以 writeheader() 自動生成標頭列。   
PNG
#### ● 編碼相容性（utf-8-sig）：寫入 CSV 時指定 utf-8-sig（帶有 BOM 的 UTF-8），避免微軟 Excel 在開啟含有非 ASCII 字元或特殊標點時發生亂碼。

## 5. HTTP 連線與編碼管理（requests 模組）
#### ● 連線編碼校正：在解析 HTML 前顯式指定 response.encoding = "utf-8"，確保抓取回來的 HTML 文字編碼與目標網站宣告一致，防止解析過程中出現解碼錯誤。

<img width="1850" height="305" alt="image" src="https://github.com/user-attachments/assets/4074828e-7392-4e30-a7da-926bdc7f8e2b" />
