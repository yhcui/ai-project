import openai
from openai import OpenAI

client = openai.OpenAI(api_key="sk-",base_url="https://api.siliconflow.cn/v1")
response = client.chat.completions.create(model='Pro/deepseek-ai/DeepSeek-R1', messages=[
        {"role": "user",
        "content": "推理模型会给市场带来哪些新的机会"}
    ],
    stream=True
)
print(response)
for chunk in response:
    print(chunk.id)
    print(chunk.model)
    if not chunk.choices:
        continue
    if chunk.choices[0].delta.content:
        print("1-------------------------------------")
        print(chunk.choices[0].delta.content, end="", flush=True)
    reasoning = getattr(chunk.choices[0].delta, 'reasoning_content', None)
    if reasoning:
        print("2-------------------------------------")
        print(reasoning, end="", flush=True)