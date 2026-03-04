# 🔐 Password Strength Checker (CLI Tool)

A lightweight **Python command-line tool** that analyzes password strength and generates **cryptographically secure passwords**.

This project demonstrates how password security tools work and is designed as a **cybersecurity learning project**.

---

# 🚀 Features

* ✔ Check password strength instantly
* ✔ Generate secure random passwords
* ✔ Uses Python's **cryptographically secure ****`secrets`**** module**
* ✔ Simple **command-line interface (CLI)**
* ✔ Lightweight and beginner friendly
* ✔ Works on **Linux, Windows, and macOS**

---

# 📦 Step-by-Step Installation

## 1️⃣ Install Python

Make sure Python **3.6 or higher** is installed.

Check your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

If Python is not installed, download it from:

https://www.python.org/downloads/

---

## 2️⃣ Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/RishuRana2867/password-strength-checker.git
```

Move into the project folder:

```bash
cd password-strength-checker
```

---

## 3️⃣ (Optional) Create a Virtual Environment

Linux / macOS:

```bash
python3 -m venv venv
```

Windows:

```bash
python -m venv venv
```

Activate it:

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## 4️⃣ Install Requirements

This project only uses **Python standard libraries**, so no external packages are required.

But you can still run:

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run the Tool

```bash
python strength_checker.py -h
```

You should see the help menu.

---

# 🛠 Usage

## Check Password Strength

```bash
python strength_checker.py -c MyPassword123!
```

Example Output:

```
[+] Password: MyPassword123!
[+] Strength : STRONG
```

---

## Generate Secure Password

```bash
python strength_checker.py -g 16
```

Example Output:

```
[+] Generated Password: aB$9k!2LmQ@1pRz7
```

---

# ⚙ Command Options

| Option | Description                |
| ------ | -------------------------- |
| `-c`   | Check password strength    |
| `-g`   | Generate a secure password |
| `-h`   | Show help menu             |

Example:

```bash
python strength_checker.py -c password123
```

```bash
python strength_checker.py -g 12
```

---

# 🔍 Password Strength Criteria

The tool evaluates passwords based on:

* Password length (8+ characters)
* Lowercase letters
* Uppercase letters
* Numbers
* Special characters

Strength levels:

* **Weak**
* **Medium**
* **Strong**

---

# 📂 Project Structure

```
password-strength-checker
│
├── strength_checker.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# 📋 Requirements

Python **3.6+**

This tool uses only Python **built-in modules**:

```
string
secrets
argparse
```

No external dependencies are required.

---

# 💡 Example

```
$ python strength_checker.py -c password123
[+] Password: password123
[+] Strength : MEDIUM
```

```
$ python strength_checker.py -g 12
[+] Generated Password: @G7!kL9$wPq1
```

---

# 🔮 Future Improvements

Possible improvements for this project:

* Password entropy calculation
* Colored terminal output
* Password breach checking
* Dictionary attack simulation
* GUI version of the tool

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

Created as a **Python cybersecurity learning project** to practice building security tools and command-line utilities.
