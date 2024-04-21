import requests

def answer_question(question):
  # Replace with your Bard endpoint (if different)
  url = "https://your-bard-endpoint/questions"  
  payload = {"question": question}
  response = requests.post(url, json=payload)
  return response.json()["answer"]

# Example usage
question = "What is the capital of France?"
answer = answer_question(question)
print(answer)  # Output: Paris (expected)
