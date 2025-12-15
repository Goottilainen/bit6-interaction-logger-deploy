from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def process():
    data = request.get_json()

    if not data or "text" not in data or not data["text"].strip():
        return jsonify({"error": "Empty input"}), 400

    return jsonify({
        "result": f"Processed response: {data['text'].strip()}"
    })
