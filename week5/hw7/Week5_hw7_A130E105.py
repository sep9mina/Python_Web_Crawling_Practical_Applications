import re

phones = [
    "+886912-345-678",
    "+886 922 111 886",
    "0928 888-666",
    "0966-123-345",
]

# ① 開頭的 +886 轉換成 0（包含可能緊接在後的空格）
step1 = [re.sub(r"^\+886\s*", "0", p) for p in phones]
print(f"① {step1}")

# ② 刪掉數字以外的符號（如 -、空白等）
step2 = [re.sub(r"\D", "", p) for p in step1]
print(f"② {step2}")

# ③ 利用 re.fullmatch 檢查清理前、後，是否為 09 開頭的 10 碼數字
pattern = r"09\d{8}"
check_before = [bool(re.fullmatch(pattern, p)) for p in phones]
check_after = [bool(re.fullmatch(pattern, p)) for p in step2]
print(f"③ 清理前 {check_before}")
print(f"  清理後 {check_after}")

# ④ 利用 re.sub 的 count 參數，將前 6 碼替換為星號，只保留末 4 碼
step4 = [re.sub(r"\d", "*", p, count=6) for p in step2]
print(f"④ {step4}")