from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from utils.image_enhancer import enhance_image

app = Flask(__name__) # Initialize Flask app


# Define folders to store uploaded and processed images
UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Allowed image formats for upload
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

progress = {"value": 0}


# Helper function to check if uploaded file is valid
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Home route - renders the main upload page
@app.route("/")
def home():
    return render_template("index.html")

# Route to fetch current progress
@app.route("/progress")
def get_progress():
    return jsonify(progress)


# Route to handle file upload and processing
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if file is None or file.filename == "":
        return "No file selected"

# Check file type
    if not allowed_file(file.filename):
        return "Only JPG, JPEG, PNG images are supported"

    filename = secure_filename(file.filename)

    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_filename = "enhanced_" + filename
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    file.save(input_path)

    progress["value"] = 0

    try:
        enhance_image(input_path, output_path, progress)
    except Exception as e:
        progress["value"] = 0
        return f"Error during processing: {str(e)}"

  # After processing, show result page with original & enhanced image
    return render_template(
        "result.html",
        original=filename,
        enhanced=output_filename
    )


if __name__ == "__main__":
    app.run(debug=True)