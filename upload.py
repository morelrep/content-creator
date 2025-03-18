from flask import Flask, request, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".csv"):
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], "books_zotero.csv")
            file.save(file_path)
            return "File uploaded successfully!"
        else:
            return "Invalid file type. Please upload a CSV."
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
