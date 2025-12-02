import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import markdown

from flask import Flask, Response, render_template, request, jsonify
from tutor.tutor_core import AITutor

app = Flask(__name__)
tutor = AITutor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream", methods=["POST"])
def stream():
    data = request.get_json()
    user_message = data.get("message", "")

    def generate():
        for chunk in tutor.stream(user_message):
            yield f"data: {chunk}\n\n"

        yield "data: [DONE]\n\n"

    return Response(generate(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True)