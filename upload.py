from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = "assets/data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

SCRIPT_PATH = "python3 assets/env/src/morel-generate.py"  # Replace with your actual script filename

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".csv"):
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], "books_zotero.csv")
            file.save(file_path)
            
            # Run the script to generate output
            result = subprocess.run(
    ["python", "morel-generate.py"], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE, 
    text=True, 
    cwd="assets/env/src"
)
            
            return f"File uploaded and processed!<br><pre>{result.stdout}</pre>"
        else:
            return "Invalid file type. Please upload a CSV."
    
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload and Process">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
