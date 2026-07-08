from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download-cv")
def download_cv():
    """Serve the CV file for download. Place your CV as 'cv.pdf' in the static folder."""
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "cv.pdf",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
