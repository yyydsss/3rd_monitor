# Call the server using curl:
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
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
							"url": "http://localhost:9000/record3.jpg"
						}
					}
				]
			}
		]
	}'