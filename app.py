from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running"

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    return jsonify(received=data)

if __name__ == "__main__":
    app.run(debug=True)
