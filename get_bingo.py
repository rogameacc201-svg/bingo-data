import requests
import json
import time

def get_bingo_json():
    # 這是公開的彩券 API 接口
    url = "https://api.taiwanlottery.com.tw/BingoBingo/Result"
    
    try:
        # 增加 headers，讓請求更像正規 API 呼叫
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Content-Type": "application/json"
        }
        
        # 使用 requests.get 獲取數據
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            # 直接解析 JSON
            data = response.json()
            # 假設結構如下 (根據台彩原始資料格式)
            with open("bingo_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
            print(f"[{time.strftime('%H:%M:%S')}] JSON 資料獲取成功！")
        else:
            print(f"伺服器回應錯誤: {response.status_code}")
            
    except Exception as e:
        print(f"無法存取 JSON API: {e}")

get_bingo_json()