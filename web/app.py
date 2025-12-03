import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify
from tutor.tutor_core import AITutor

app = Flask(__name__)
tutor = AITutor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message", "")
    reply = tutor.chat(user_message)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)