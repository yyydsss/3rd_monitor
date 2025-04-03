import requests
import threading
import time
import statistics
from concurrent.futures import ThreadPoolExecutor
from typing import List, Optional

def call_qwen_vl_api(req_id: int) -> Optional[float]:
    url = "http://localhost:8000/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "Qwen/Qwen2.5-VL-7B-Instruct-AWQ",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "提取标签的关键信息并返回json格式"},
                    {
                        "type": "image_url",
                        "image_url": {"url": "http://localhost:9000/label.jpg"}
                    }
                ]
            }
        ]
    }

    start_time = time.time()
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        elapsed_time = time.time() - start_time
        print(f"Request {req_id} - Status: {response.status_code}, Time: {elapsed_time:.2f}s")
        if response.status_code == 200:
            print(f"Response {req_id} (Partial): {str(response.json())[:200]}...")  # 截断长输出
        else:
            print(f"Error {req_id}: {response.text}")
        return elapsed_time
    except Exception as e:
        print(f"Request {req_id} failed: {str(e)}")
        return None

def measure_avg_response_time_threaded(num_requests: int = 5) -> float:
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        # 提交所有任务到线程池
        futures = [executor.submit(call_qwen_vl_api, i+1) for i in range(num_requests)]
        response_times: List[Optional[float]] = [future.result() for future in futures]

    valid_times = [t for t in response_times if t is not None]
    if not valid_times:
        raise ValueError("All requests failed!")

    avg_time = statistics.mean(valid_times)
    print(f"\nAverage Response Time (Threaded): {avg_time:.2f}s (over {len(valid_times)} requests)")
    return avg_time

if __name__ == "__main__":
    measure_avg_response_time_threaded()