import cohere


api_key = "your api key here"

co = cohere.ClientV2(api_key=api_key)
response = co.chat(
    model="command-a-plus-05-2026",
    messages=[{"role": "system", "content": "Responde en castellano con emojis y mucha alegria"},
    {"role": "user", "content": "Tell me about LLMs"},
    {"role": "assistant", "content": "THEY ARE GREAT"},
    {"role": "user", "content": "Repeat your last message"}],
)
print(response.message.content[1].text)