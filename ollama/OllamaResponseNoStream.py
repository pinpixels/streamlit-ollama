from ollama import generate

response = generate('phi3:latest', 'Why is the sky blue?')
print(response['response'])
