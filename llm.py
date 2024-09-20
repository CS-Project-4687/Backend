from dotenv import load_dotenv
import os
load_dotenv()

from groq import Groq

client = Groq(
    api_key=os.getenv("API_KEY"),
)

system = ""
with open('SystemPrompt.txt', 'r') as file:
    system = file.read()

def createTT(q):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system
        },
        {
            "role": "user",
            "content": q
        }
    ],
    model="llama3-8b-8192",
    )
    response = []

    for i in chat_completion.choices[0].message.content.split("\n"):
        response.append(i.split("=>"))

    return response