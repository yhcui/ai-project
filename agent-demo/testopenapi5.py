import openai
from openai import OpenAI

client = openai.OpenAI(api_key="sk-",base_url="https://api.siliconflow.cn/v1")
response = client.chat.completions.create(
    model="Pro/zai-org/GLM-5.1",
    messages=[
        {"role": "user",
         "content": "SiliconFlow公测上线，每用户送3亿token 解锁开源大模型创新能力。对于整个大模型应用领域带来哪些改变？"}
    ],
    stream=True  # 启用流式输出
)

for chunk in response:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta

    reasoning_content = getattr(delta, "reasoning_content",None)
    content = getattr(delta, "content",None)

    if reasoning_content:
        print(reasoning_content, end="", flush=True)
    if content:
        print(content, end="", flush=True)
    print()