import requests

# 1. 目標網址
URL = "https://www.scrapethissite.com/pages/forms/"

# 2. 設定 Request Headers（模擬瀏覽器發送請求）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 3. 發送 GET 請求
resp = requests.get(URL, headers=HEADERS, timeout=10)

# 4. 解析 Response 伺服器回應內容
print(f"[Response] 狀態碼: {resp.status_code}")
print(f"[Response] Content-Type: {resp.headers.get('Content-Type')}")
print(f"[Response] 編碼: {resp.encoding}")
print(f"[Response] 花費秒數: {resp.elapsed.total_seconds()} 秒")
print(f"[Response] User-Agent: {resp.request.headers.get('User-Agent')}")
