import pandas as pd

# 原始 log 文字資料（若讀取檔案可用 with open(...)）
log_data = """INFO 2026-10-20: Start crawling quotes.toscrape.com
INFO 2026-10-20: Saved 10 quotes to authors.csv
WARNING 2026-10-20: Tag not found in quote 3
ERROR 2026-10-20: Connection timed out
ERROR: 2026-10-21: Retry failed
ERROR 2026-10-21: 404 Not Found /author/Albert-Einsten"""

lines = log_data.strip().splitlines()

# --------------------------------------------------
# ① 每一行拆成 dict (level、date、message)
# --------------------------------------------------
records = []
for line in lines:
    # 觀察格式："[LEVEL] [DATE]: [MESSAGE]"
    # 先以冒號加空格 (": ") 拆出前面與訊息本體
    parts = line.split(": ", 1)
    if len(parts) == 2:
        prefix, message = parts[0], parts[1]
        prefix_parts = prefix.split()
        
        # 標準格式應該拆成 [LEVEL, DATE]
        if len(prefix_parts) == 2:
            level = prefix_parts[0]
            date = prefix_parts[1]
            records.append({
                "level": level,
                "date": date,
                "message": message
            })
        # 若需要相容包含 "ERROR: 2026-10-21: Retry failed" 這種格式：
        # elif len(prefix_parts) == 1 and prefix_parts[0].endswith(':'): ...
        # 但從預期輸出看，該異常格式未出現在最終 DataFrame 中

# --------------------------------------------------
# ② 把 dict 轉成 DataFrame
# --------------------------------------------------
df = pd.DataFrame(records)
print("=== ② DataFrame 輸出 ===")
print(df)
print()

# --------------------------------------------------
# ③ 統計各等級筆數、列出所有 ERROR 訊息
# --------------------------------------------------
print("=== ③-1 各等級筆數統計 ===")
print(df["level"].value_counts())
print()

print("=== ③-2 所有 ERROR 訊息 ===")
error_messages = df[df["level"] == "ERROR"]["message"].tolist()
for msg in error_messages:
    print("-", msg)