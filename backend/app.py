from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
messages_file = os.path.join(os.path.dirname(__file__), "messages.txt")

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    name = data.get("name", "Anonymous")
    class_info = data.get("class", "Anonymous")
    message = data.get("message", "")
    if not message.strip():
        return jsonify({"status": "error", "message": "Empty message"}), 400
    with open(messages_file, "a", encoding="utf-8") as f:
        f.write(f"Name: {name}\nClass: {class_info}\nMessage: {message}\n{'-'*30}\n")

    return jsonify({"status": "success", "message": "Message saved!"}), 200


if __name__ == "__main__":
    # Roda o servidor local
    app.run(debug=True)

