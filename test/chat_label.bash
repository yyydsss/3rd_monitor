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
						"text": "提取几条关键信息并且输出json格式（同样的字段只输出一次就可以了）"
					},
					{
						"type": "image_url",
						"image_url": {
							"url": "http://localhost:9000/label4.jpg"
						}
					}
				]
			}
		]
	}'