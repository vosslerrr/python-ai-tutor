import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import markdown

from flask import Flask, render_template, request, jsonify
from tutor.tutor_core import AITutor

app = Flask(__name__)
tutor = AITutor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json["message"]

    raw_reply = tutor.auto(user_message)

    html_reply = markdown.markdown(
        raw_reply,
        extensions=["fenced_code", "tables", "nl2br"]
    )

    return jsonify({"reply": html_reply})

if __name__ == "__main__":
    app.run(debug=True)
