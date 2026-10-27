<img width="1529" height="836" alt="image" src="https://github.com/user-attachments/assets/3bca1b96-65e0-473a-a70e-9bc547fef8bf" />

<img width="642" height="845" alt="image" src="https://github.com/user-attachments/assets/d0813e7e-6f85-4cda-9864-749ba50cec17" />

## 正規表達式文字清理（re.sub）：
### 錨點與字元匹配：使用 ^ 錨定開頭替換特定國碼（+886），並透過跳脫字元 \+ 與空白符號 \s* 處理不同格式的間距。

## 反向字元類別（\D）：
### 利用 \D 匹配所有非數字字元並進行批次移除，快速完成資料清洗與格式標準化。

## 替換次數限制（count 參數）：
### 利用 re.sub() 的 count 參數控制僅替換前 $N$ 個符合條件的字元，以簡潔的語法完成資料遮罩（Masking）與個資去識別化。

## 精確模式比對與資料驗證（re.fullmatch）：
### 字元長度與量詞控制：透過 09\d{8} 搭配 fullmatch，嚴格檢查整個字串是否恰為「以 09 開頭且總長為 10 碼的純數字」，而非僅部分符合。

## 布林轉換驗證：
### 利用 bool(match_obj) 將比對結果（Match 物件或 None）直接轉換為布林值（True/False），達到資料格式驗證（Data Validation）的目的。

## Python 串列生成式（List Comprehension）：
### 以宣告式語法對陣列元素進行批次轉換與比對，取代傳統的 for 迴圈與 append，提升程式碼可讀性與執行效率。
