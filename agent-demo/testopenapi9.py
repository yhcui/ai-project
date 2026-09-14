from time import sleep

import openai
from openai import OpenAI

client = openai.OpenAI(api_key="sk-",base_url="https://api.siliconflow.cn/v1")

response = client.images.generate(
    model="Kwai-Kolors/Kolors",
    prompt="生成一张美女",
    size="1024x1024",
    n=1,
    extra_body= {
        "step":20
    }
)
print(response)