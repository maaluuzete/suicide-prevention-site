from flask import Flask, render_template, request, jsonify, send_from_directory
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")
TEMPLATES_DIR = os.path.join(FRONTEND_DIR, "templates")

app = Flask(__name__, static_folder=FRONTEND_DIR, template_folder=TEMPLATES_DIR)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/talk")
def talk():
    return render_template("talk.html")

@app.route("/healthy")
def healthy():
    return render_template("healthy.html")

@app.route("/emotional_empathy")
def emotional_empathy():
    return render_template("emotional_empathy.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/save", methods=["POST"])
def save_message():
    data = request.get_json()
    name = data.get("name", "Anonymous")
    classInfo = data.get("classInfo", "Anonymous")
    message = data.get("message", "")

    messages_path = os.path.join(BASE_DIR, "messages.txt")
    print(f"📩 Salvando mensagem em: {messages_path}")

    try:
        with open(messages_path, "a", encoding="utf-8") as file:
            file.write(f"Name: {name}\nClass: {classInfo}\nMessage: {message}\n{'-'*40}\n")
        print("✅ Mensagem salva com sucesso!")
        return jsonify({"success": True})
    except Exception as e:
        print(f"❌ Erro ao salvar mensagem: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)

@app.route("/assets/<path:filename>")
def serve_assets(filename):
    assets_dir = os.path.join(BASE_DIR, "..", "assets")
    return send_from_directory(assets_dir, filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

