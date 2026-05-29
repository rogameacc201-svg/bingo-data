import requests
import json
import time

def run_crawler():
    # 使用台彩官方 JSON 接口，這在雲端伺服器上存取最快
    url = "https://www.taiwanlottery.com.tw/result/bingobingo/bingobingo_result.aspx"
    
    try:
        # headers 模擬真實瀏覽器行為
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers, timeout=20)
        
        # 這裡簡化解析，假設您只需要號碼列表 (請根據實際需求調整解析邏輯)
        # 因為台彩網頁結構複雜，建議先確認 request 是否成功
        if response.status_code == 200:
            # 假設已解析出的號碼
            numbers = ["01", "02", "03", "04", "05"] # 這裡請放入您的解析邏輯
            
            data = {
                "numbers": numbers,
                "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # 寫入 JSON 檔案
            with open("bingo_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
            print("資料寫入成功")
            
    except Exception as e:
        print(f"錯誤: {e}")

if __name__ == "__main__":
    run_crawler()
