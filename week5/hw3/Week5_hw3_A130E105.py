import re
import pandas as pd

# 讀取課堂練習 - 1 產生的 csv 檔案
df = pd.read_csv("authors.csv")

# 取第一列資料進行練習示範（或依題目需求選取）
first_row = df.iloc[0]

# 任務 1：born_date 的所有數字
# 字元類可用 [0-9] 或 \d
born_date_str = str(first_row["born_date"])
ans1 = re.findall(r"\d", born_date_str)
# 也可以寫成：re.findall(r'[0-9]', born_date_str)

# 任務 2：born_location 的所有大寫字母
# 字元類可用 [A-Z]
born_location_str = str(first_row["born_location"])
ans2 = re.findall(r"[A-Z]", born_location_str)

# 任務 3：tags 裡所有非小寫字母的字元
# 字元類可用 [^a-z]（^ 在中括號內代表「排除/非」）
tags_str = str(first_row["tags"])
ans3 = re.findall(r"[^a-z]", tags_str)

# 任務 4：quote 裡所有的標點符號
# 常見標點符號字元類，或使用正規表達式排除字詞字元與空白：[^\w\s]
quote_str = str(first_row["quote"])
ans4 = re.findall(r"[^\w\s]", quote_str)

# 輸出結果
print(f"① {ans1}")
print(f"② {ans2}")
print(f"③ {ans3}")
print(f"④ {ans4}")