import openai
from openai import OpenAI

client = openai.OpenAI(api_key="sk-",base_url="https://api.siliconflow.cn/v1")
response = client.chat.completions.create(
    model="Pro/moonshotai/Kimi-K2.6",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://www.xindecoaiot.com/assets/images/about4.jpg",
                    },
                },
                {
                    "type": "text",
                    "text": "这个图片内容是什么？"
                }
            ],
        }
    ],
    temperature=0.7,
    max_tokens=1024,
    stream=True
)

for chunk in response:
    if not chunk.choices:
        continue
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
    # if chunk.choices[0].delta.reasoning_content:
    #     print(chunk.choices[0].delta.reasoning_content, end="", flush=True)

# for chunk in response:
#     if not chunk.choices:
#         continue
#     if chunk.choices[0].delta.content:
#         print(chunk.choices[0].delta.content)
#     if chunk.choices[0].delta.reasoning_content:
#         print(chunk.choices[0].delta.reasoning_content, end="", flush=True)