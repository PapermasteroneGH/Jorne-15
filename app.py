from flask import Flask, request, jsonify
from flask_cors import CORS
import openai  # Example AI Model

app = Flask(__name__)
CORS(app)  # Allow requests from Chrome Extension

# Load AI Model (Example with OpenAI)
openai.api_key = "your-api-key"

@app.route("/process", methods=["POST"])
def process_text():
    data = request.json
    user_input = data.get("text", "")

    # AI Processing (GPT Example)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
