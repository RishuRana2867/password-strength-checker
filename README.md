# Password Strength Checker

A lightweight **Python CLI tool** that analyzes password strength and generates **cryptographically secure passwords** to help improve user security.

---

## Features

* Check password strength instantly
* Generate secure random passwords
* Uses Python's `secrets` module for strong randomness
* Simple **command-line interface**
* Lightweight and beginner-friendly
* Works on **Linux, Windows, and macOS**

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/RishuRana2867/password-strength-checker.git
cd password-strength-checker
```

### 2. Run the tool

```bash
python strength_checker.py -h
```

---

## Usage

### Check Password Strength

```bash
python strength_checker.py -c MyPassword123!
```

Example output:

```
[+] Password: MyPassword123!
[+] Strength : STRONG
```

---

### Generate a Secure Password

```bash
python strength_checker.py -g 16
```

Example output:

```
[+] Generated Password: aB$9k!2LmQ@1pRz7
```

---

## Command Options

| Option               | Description                |
| -------------------- | -------------------------- |
| `-c` or `--check`    | Check password strength    |
| `-g` or `--generate` | Generate a secure password |
| `-h` or `--help`     | Show help menu             |

---

## Password Strength Criteria

The tool evaluates passwords based on:

* Minimum length (8+ characters)
* Lowercase letters
* Uppercase letters
* Numbers
* Special characters

Passwords are categorized as:

* **Weak**
* **Medium**
* **Strong**

---

## Project Structure

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

## Requirements

Python **3.6 or higher**

The following modules are used:

```
string
secrets
argparse
```

All of these are **built into Python**, so no additional installation is required.

---

## Example

```
$ python strength_checker.py -c password123
[+] Password: password123
[+] Strength : MEDIUM
```

---

## Future Improvements

Possible features to add:

* Password entropy calculation
* Colorized terminal output
* Password breach checking (HaveIBeenPwned API)
* Wordlist attack simulation
* GUI version of the tool

---

## License

This project is licensed under the **MIT License**.

---

## Author

Created as a **Python cybersecurity learning project**.
