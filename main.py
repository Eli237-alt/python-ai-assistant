import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("AI Question & Answer Assistant")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = client.responses.create(
        model="gpt-6.2-astra",
        input=question
    )

    print("\nAI:", response.output_text)
    print()