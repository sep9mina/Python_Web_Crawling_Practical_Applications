<img width="1663" height="750" alt="image" src="https://github.com/user-attachments/assets/9d880948-b740-4918-84f9-61fc8e5ed6ea" />

## 爬取台灣資料並匯出
<img width="979" height="310" alt="image" src="https://github.com/user-attachments/assets/debe3bb7-8036-4abc-a373-fce6476c3359" />

## 相依套件：執行前請確認已安裝所需套件：
##### python -m pip install requests beautifulsoup4 pandas openpyxl
####
#### HTML 結構定位：
#### 卡片容器：&lt;div class="col-md-4 country"&gt;
#### 國家名稱：&lt;h3 class="country-name"&gt;
#### 首都：&lt;span class="country-capital"&gt;
#### 人口：&lt;span class="country-population"&gt;
#### 面積：&lt;span class="country-area"&gt;
#### 寫入 Excel：使用 Pandas 的 to_excel() 函式，若不需要保留預設數字索引，設定 index=False 即可讓產出的表格更乾淨。

<img width="1152" height="302" alt="image" src="https://github.com/user-attachments/assets/d49609b5-5c27-411f-a97a-0712a2c5cc47" />
