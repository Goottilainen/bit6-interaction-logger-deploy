from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode="require"   
    )




@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "API is running"})


@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    user_prompt = data["text"]

    ai_response = f"AI response to: {user_prompt}"

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

    return jsonify({
        "prompt": user_prompt,
        "response": ai_response
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
