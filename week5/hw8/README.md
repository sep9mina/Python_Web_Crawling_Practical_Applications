<img width="1584" height="753" alt="image" src="https://github.com/user-attachments/assets/a9bbc003-fcc6-4d1d-b1c9-f4c303570413" />

<img width="685" height="903" alt="image" src="https://github.com/user-attachments/assets/999f566f-5ef6-4f6f-844e-66987b219a89" />

<img width="604" height="289" alt="image" src="https://github.com/user-attachments/assets/37a18cec-6a2a-44d4-9215-4726941a99de" />

<img width="563" height="368" alt="image" src="https://github.com/user-attachments/assets/3ce459b8-f83f-48a5-8838-4a7dea73e7c9" />

## 正規表達式字串替換與清理（re.sub）：
#### 字首特徵替換：利用 ^ 錨定開頭結合跳脫符號 \+ 與空白符號 \s*，精準將 +886 格式轉換為本地碼 0。

## 非數字字元清除：
#### 使用反向字元類別 \D（匹配所有非數字），批次剃除非數字符號（如 - 與空格），完成標準化清理。

## 次數限定遮罩：
#### 運用 count=6 參數限制替換次數，僅遮蔽前 6 碼數字為 *，保留末 4 碼以達成個資去識別化。

## 精確格式驗證（re.fullmatch）：
#### 使用 09\d{8} 比對「09 開頭且總長度恰為 10 碼」的規則。 透過 fullmatch 嚴格確保全字串完全吻合，避免 search 或 match 可能產生的部分匹配問題。

## 布林轉換機制（Type Casting）：
#### 配合 bool() 將比對成功產生的 Match 物件轉換為 True、未吻合的 None 轉換為 False，快速產出資料驗證結果。

## Python 串列生成式（List Comprehension）：
#### 使用 [func(x) for x in list] 取代傳統多行的 for 迴圈與 append()，讓批次資料處理的程式碼更簡潔且具備更佳的執行效能。
