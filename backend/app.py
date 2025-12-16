from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_db_connection():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise Exception("DATABASE_URL NOT FOUND AT RUNTIME")

    return psycopg2.connect(database_url)


def init_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS prompts (
                id SERIAL PRIMARY KEY,
                user_prompt TEXT NOT NULL,
                ai_response TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("DB ready: table 'prompts' exists")
    except Exception as e:
        print("DB init failed:", e)

def get_ai_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return completion.choices[0].message.content
    except Exception as e:
        print("AI error:", e)
        return "AI service temporarily unavailable."


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "API is running"})


@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    user_prompt = data["text"]

    ai_response = get_ai_response(user_prompt)

    db_saved = False
    db_error = None

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO prompts (user_prompt, ai_response)
            VALUES (%s, %s)
            """,
            (user_prompt, ai_response),
        )
        conn.commit()
        cur.close()
        conn.close()
        db_saved = True
    except Exception as e:
        db_error = str(e)

    return jsonify({
        "prompt": user_prompt,
        "response": ai_response,
        "db_saved": db_saved,
        "db_error": db_error
    })


if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
