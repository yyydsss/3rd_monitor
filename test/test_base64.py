import requests
import json
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# 本地图片路径
image_path = "/mnt/mnt/record3.jpg"  # 替换为你的图片路径

# 将图片转换为base64
image_base64 = image_to_base64(image_path)

url = "http://localhost:8000/v1/chat/completions"

headers = {
    "Content-Type": "application/json"
}

data = {
    "model": "Qwen/Qwen2.5-VL-7B-Instruct-AWQ",
    "temperature": 0,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "判断图中的文件是否有相关人员的签名，只输出一个token表明是或者否"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        # 使用data URI scheme直接嵌入base64图片数据
                        "url": f"data:image/jpeg;base64,{image_base64}"
                    }
                }
            ]
        }
    ]
}

try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    print("Response:", response.json())
except requests.exceptions.RequestException as e:
    print(f"请求错误: {e}")
except json.JSONDecodeError as e:
    print(f"JSON解析错误: {e}")