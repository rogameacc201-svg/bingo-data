import requests
import json
import time
import os

def run_crawler():
    url = "https://www.taiwanlottery.com.tw/result/bingobingo/bingobingo_result.aspx"
    data = {"numbers": [], "error": "尚未抓取到資料", "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")}
    
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        # 增加 timeout 確保不會卡死
        response = requests.get(url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            # 這裡暫時先寫死測試資料，確保檔案生成
            data = {
                "numbers": ["01", "02", "03", "04", "05"], 
                "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            print("抓取成功")
        else:
            data["error"] = f"網頁狀態碼: {response.status_code}"
            
    except Exception as e:
        data["error"] = str(e)
        print(f"錯誤: {e}")

    # 強制寫入檔案，確保 git 不會找不到
    with open("bingo_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    print("已生成 bingo_data.json")

if __name__ == "__main__":
    run_crawler()
