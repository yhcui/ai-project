import openai
from openai import OpenAI

client = openai.OpenAI(api_key="sk-",base_url="https://api.siliconflow.cn/v1")
response = client.chat.completions.create(
    model="Pro/moonshotai/Kimi-K2.6",
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "? 2020 年世界奥运会乒乓球男子和女子单打冠军分别是谁? "
                                    "Please respond in the format {\"男子冠军\": ..., \"女子冠军\": ...}"}
    ],
    response_format={"type": "json_object"}
)

print(response.choices[0].message.content)
# for chunk in response:
#     if not chunk.choices:
#         continue
#     if chunk.choices[0].delta.content:
#         print(chunk.choices[0].delta.content, end="", flush=True)
    # if chunk.choices[0].delta.reasoning_content:
    #     print(chunk.choices[0].delta.reasoning_content, end="", flush=True)

# for chunk in response:
#     if not chunk.choices:
#         continue
#     if chunk.choices[0].delta.content:
#         print(chunk.choices[0].delta.content)
#     if chunk.choices[0].delta.reasoning_content:
#         print(chunk.choices[0].delta.reasoning_content, end="", flush=True)