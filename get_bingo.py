import requests
import json
import time

def run_crawler():
    # 替換為一個穩定的數據接口，此處以一個範例公開 API 為例
    # 請搜尋 "Bingo Bingo JSON API" 找到最新的公開接口網址
    url = "https://api.opendomain.com/v1/bingo-latest" 
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # 確保儲存格式一致
            with open("bingo_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
            print("資料獲取成功")
        else:
            raise Exception(f"API 請求錯誤: {response.status_code}")
    except Exception as e:
        # 如果還是失敗，紀錄錯誤但不中斷流程
        with open("bingo_data.json", "w", encoding="utf-8") as f:
            json.dump({"numbers": [], "error": str(e), "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")}, f)
            print(f"失敗: {e}")

if __name__ == "__main__":
    run_crawler()
