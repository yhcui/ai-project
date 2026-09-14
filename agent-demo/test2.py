from openai import OpenAI

client = OpenAI(api_key="sk-",base_url="https://api.siliconflow.cn/v1")
response = client.responses.create(
    model="Pro/deepseek-ai/DeepSeek-R1",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)
print(response.output_text)