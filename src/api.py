from flask import Flask
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="http://sazrocks.com:60001/v1", api_key="alskdfjlaskdjLFJKADSLJKDSFL"
)


@app.route("/")
def home():
    completion = client.chat.completions.create(
        model="llama3:8b",
        messages=[
            {"role": "system", "content": "You are an AI assistant"},
            {"role": "user", "content": ""},
        ],
    )

    return completion.choices[0].message.content
