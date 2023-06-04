import openai
openai.api_key = "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"
model_engine = "gpt-3.5-turbo" 
# This specifies which GPT model to use, as there are several models available, each with different capabilities and performance characteristics.

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, ChatGPT!"},
    ])

message = response.choices[0]['message']
print("{}: {}".format(message['role'], message['content']))