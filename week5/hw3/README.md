<img width="1576" height="716" alt="image" src="https://github.com/user-attachments/assets/26296703-5866-4369-b5e9-3fc033807b38" />

<img width="871" height="897" alt="image" src="https://github.com/user-attachments/assets/9f754fef-8240-4359-8064-e3f6c2e28f9f" />

## Python 正規表達式（Regular Expressions, Regex） 中的 「字元類（Character Classes）」 語法與應用：   
#### ● 正規表達式字元類（Character Classes）核心語法：   數字匹配：使用 [0-9] 或預定義字元集 \d，用於提取字串中的單一阿拉伯數字。
#### ● 字元範圍匹配：使用連字號 - 指定 ASCII 區間，例如 [A-Z] 匹配所有大寫英文字母。
#### ● 反向排除（Negated Character Class）：在中括號開頭加上脫字號 ^（如 [^a-z]），代表「排除該範圍外的所有字元」。
#### ● 非文字與非空白匹配：結合多個預定義字元集並進行反向匹配（如 [^\w\s]），排除掉字母、數字、底線（\w）與空白（\s），藉此精準擷取標點符號。
#### ● 字串擷取函式應用：使用 Python 內建 re.findall(pattern, string) 函式，依據規則全局比對並以列表（List）形式回傳所有相符的單一字元。
#### ● 資料處理整合：配合 pandas 套件讀取 CSV 表格欄位資料（如 born_date、born_location、tags、quote），並轉為字串格式後進行正規表達式解析。  
