from ollama import generate


for part in generate('phi3:latest', 'Why is the sky blue?', stream=True):
  print(part['response'], end='', flush=True)
  

