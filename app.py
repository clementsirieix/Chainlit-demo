from flask import Flask, render_template, request, redirect
import openai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY", "")

notes = []

init_prompt = """initial prompt"""

template = """Query: {note}"""


@app.route("/")
def home():
    return render_template("index.html", notes=notes)


@app.route("/create", methods=["POST"])
async def create_note():
    content = request.form["note"]

    tags = await tag_note(content)

    notes.append({"content": content, "tags": tags})

    return redirect("/")


async def tag_note(content: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": init_prompt,
            },
            {"role": "user", "content": template.replace("{note}", content)},
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response["choices"][0]["message"]["content"].split(", ")


if __name__ == "__main__":
    app.run(debug=True)
