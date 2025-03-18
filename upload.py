import shutil
import os
import subprocess
from flask import Flask, request, send_file

app = Flask(__name__)
UPLOAD_FOLDER = "assets/data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ZIP_FILE = "output.zip"
FOLDERS_TO_ZIP = ["_authors", "_books", "_cities", "_publishers", "_repositories", "assets/img", "_data", "assets/data"]

def create_zip():
    if os.path.exists(ZIP_FILE):
        os.remove(ZIP_FILE)
    shutil.make_archive("output", "zip", root_dir=".", base_dir=".")
    return ZIP_FILE

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".csv"):
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], "books_zotero.csv")
            file.save(file_path)

            # Run the script to generate output
            result = subprocess.run(["python", "morel-generate.py"], capture_output=True, text=True, cwd="assets/env/src")

            # Create zip file
            zip_path = create_zip()

            return f"Processing complete! <a href='/download'>Download Zip</a><br><pre>{result.stdout}\n{result.stderr}</pre>"
        else:
            return "Invalid file type. Please upload a CSV."

    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload and Process">
        </form>
    '''

@app.route("/download")
def download_file():
    return send_file(ZIP_FILE, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
