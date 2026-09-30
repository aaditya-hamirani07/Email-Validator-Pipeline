````markdown
# 📧 Email Validator Pipeline

A Python-based automation script that processes a **5,000-row CSV dataset**, validates email addresses using **Regular Expressions**, and automatically separates valid and invalid emails into different CSV files.

---

## ⚙️ Tech Stack

**Language:** Python  
**Modules:** `re`, `csv`

---

## 🔄 Pipeline

```text
fake_dataset.csv
       ↓
 Read Email Addresses
       ↓
   Regex Validation
       ↓
  ┌──────────────┐
  │              │
Valid          Invalid
  │              │
  ↓              ↓
valid_emails.csv   invalid_emails.csv
````

---

## 🔍 Validation Logic

The Regex validates the basic structure of an email address.

### Local Part

The section before `@`:

* Starts with a letter or digit
* Ends with a letter or digit
* Supports letters, digits, `_`, `.`, `%`, `+`, and `-`

### Domain Part

The section after `@`:

* Starts with a letter or digit
* Ends with a letter or digit
* Allows letters, digits, and hyphens
* Requires at least one `.`
* Uses a **2–4 letter** domain extension

Examples:

```text
user@example.com
john.smith@company.org
alex_123@test.net
```

---

## 📂 Project Structure

```text
Email-Validator-Pipeline/
│
├── fake_dataset.csv
├── valid_email_checker.py
├── valid_emails.csv
├── invalid_emails.csv
└── README.md
```

---

## ▶️ Run the Project

Clone the repository:

```bash
git clone https://github.com/aaditya-hamirani07/Email-Validator-Pipeline.git
```

Navigate into the project:

```bash
cd Email-Validator-Pipeline
```

Run the script:

```bash
python valid_email_checker.py
```

The script reads:

```text
fake_dataset.csv
```

and generates:

```text
valid_emails.csv
invalid_emails.csv
```

---

## 📊 Dataset

The project uses a **5,000-row synthetic dataset** containing a mixture of valid-looking and malformed email addresses.

Examples of invalid formats included in the dataset:

```text
@example.com
user @example.com
user@example
user@domain_com
user@.com
user@example.c
```

---

## 🧠 Key Concepts Used

```text
Python
├── Regular Expressions
├── CSV File Handling
├── Functions
├── Loops
├── Conditional Logic
└── File I/O
```

---

## 🎯 Project Goal

The goal of this project is to automate the process of **sorting and filtering large collections of email addresses**, replacing manual checking with a simple Python-based validation pipeline.

---

## 👨‍💻 Author

**Aaditya Hamirani**

[GitHub](https://github.com/aaditya-hamirani07)

```
```
