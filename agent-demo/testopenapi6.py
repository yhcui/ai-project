from openai import OpenAI

import requests
import json

url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "Pro/zai-org/GLM-5.1",  # 替换成你的模型
    "messages": [
        {
            "role": "user",
            "content": "SiliconFlow公测上线，每用户送3亿token 解锁开源大模型创新能力。对于整个大模型应用领域带来哪些改变？"
        }
    ],
    "stream": True  # 此处需要设置为stream模式
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer sk-"
}


response = requests.post(url, json=payload, headers=headers,stream=True)
# 判断请求是否成功，状态码200表示成功
if response.status_code == 200:
    # 用于存储完整的回复内容
    full_content = ""
    # 用于存储完整的推理过程内容（部分模型支持深度思考）
    full_reasoning_content = ""
    # 逐行读取流式响应数据
    for chunk in response.iter_lines():
        if chunk:
            # 将字节数据解码为字符串，并移除SSE协议中的 "data: " 前缀
            chunk_str = chunk.decode('utf-8').replace('data: ', '')
            # 判断是否为流式响应的结束标志
            if chunk_str != "[DONE]":
                # 将JSON字符串解析为字典对象
                chunk_data = json.loads(chunk_str)
                # 从响应数据中提取delta字段，包含本次增量内容
                delta = chunk_data['choices'][0].get('delta', {})
                # 获取模型回复的正文内容
                content = delta.get('content', '')
                # 获取模型的推理/思考过程内容
                reasoning_content = delta.get('reasoning_content', '')
                # 如果有正文内容，实时打印并累加到完整内容中
                if content :
                    print(content, end="", flush=True)
                    full_content += content
                # 如果有推理内容，实时打印并累加到完整推理内容中
                if reasoning_content :
                    print(reasoning_content, end="", flush=True)
                    full_reasoning_content += reasoning_content

else:
    print(response.status_code)