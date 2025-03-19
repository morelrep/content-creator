import os

FOLDERS_TO_CLEAN = ["_authors", "_books", "_cities", "_publishers", "_repositories", "assets/img", "_data", "assets/data"]
ZIP_FILE = "output.zip"

def delete_generated_files():
    """Deletes generated files but keeps .keep files."""
    for folder in FOLDERS_TO_CLEAN:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file != ".keep":  # Keep .keep files
                    os.remove(os.path.join(root, file))

    # Remove the zip file after processing
    if os.path.exists(ZIP_FILE):
        os.remove(ZIP_FILE)

    print("Generated files deleted successfully.")

if __name__ == "__main__":
    delete_generated_files()
