# Content Generator Installation Guide

This guide will help you set up the program on a new system.

## **Prerequisites**

Before installing, make sure you have:

- **Python 3.12+** installed
- **Git** installed (optional, for cloning the repository)
- A terminal or command prompt with access to bash commands (Linux, macOS, or WSL on Windows)

---

## **Step 1: Clone the Repository**

If you haven't already, download the project files using Git:

```bash
git clone https://github.com/morelrep/content-generator.git
cd content-generator
```

Or, if you downloaded a ZIP file, **extract it** and navigate to the folder.

---

## **Step 2: Create a Virtual Environment**

To ensure all dependencies are installed in isolation, create a virtual environment inside the project:

```bash
python3 -m venv assets/env
```

Activate the environment:

- **Linux/macOS:**
  ```bash
  source assets/env/bin/activate
  ```
- **Windows (PowerShell):**
  ```powershell
  assets\env\Scripts\Activate
  ```

You should now see `(env)` in your terminal, indicating that the virtual environment is active.

---

## **Step 3: Install Dependencies**

Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

This will install all necessary Python libraries for the project.

---

## **Step 4: Run the Program**

To execute the program, use the following command:

```bash
python assets/src/morel-generate.py
```

This will process the necessary files and generate the expected output.

---

## **Troubleshooting**

- **"Command not found" errors?** Ensure you activated the virtual environment.
- **Missing dependencies?** Try running:
  ```bash
  pip install --upgrade pip setuptools wheel
  pip install -r requirements.txt
  ```
- **Still having issues?** Contact the project maintainer or open an issue on GitHub.

---

## **Updating and upgrading the Project**

If you need to update the project files, run:

```bash
git pull origin main
```

Then, reactivate the virtual environment and reinstall dependencies:

```bash
source assets/env/bin/activate
pip install -r requirements.txt
```

---

## **Additional Notes**

- When you update the project the virtual environment (`assets/env/`) is **ignored by Git**, so each user must create their own.
- For a clean update, delete `assets/env/`, recreate it, and reinstall dependencies.