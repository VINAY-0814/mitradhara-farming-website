from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend requests

# Load HuggingFace model (small model for free usage)
chatbot = pipeline("text-generation", model="distilgpt2")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    response = chatbot(user_message, max_length=200, num_return_sequences=1)
    reply = response[0]["generated_text"]

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)