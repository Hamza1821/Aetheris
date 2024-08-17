import openai

client = openai.OpenAI(api_key="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")

model = "gpt-3.5-turbo"  # Use a valid model name
temperature = 0.3
max_token = 500
messages = [
    {"role": "system", "content": "suppose you are a professional poet"},
    {"role": "user", "content": "write a poem on the topic the last sunset"}
]


completion = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=temperature,
    max_tokens=max_token
)
ans = completion.choices[0].message["content"]
print(ans)

