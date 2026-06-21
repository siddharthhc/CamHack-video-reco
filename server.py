from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "video" not in request.files:
        return jsonify({
            "success": False,
            "message": "No video received"
        })

    video = request.files["video"]

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".webm"

    save_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    video.save(save_path)

    print("Saved:", filename)

    return jsonify({
        "success": True,
        "filename": filename
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
