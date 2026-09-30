# 📧 Email Validator Pipeline

A simple Python automation pipeline that processes a **5,000-row CSV dataset**, validates email addresses using **Regular Expressions (Regex)**, and automatically separates them into **valid** and **invalid** CSV files.

## 🚀 Features

* 📂 Reads email data from a CSV file
* 🔍 Validates email addresses using Regex
* ✅ Separates valid email addresses
* ❌ Separates invalid email addresses
* 📄 Automatically generates separate CSV output files
* ⚡ Lightweight and easy to run

## 🛠️ Tech Stack

| Technology | Usage                                     |
| ---------- | ----------------------------------------- |
| **Python** | Core programming language                 |
| **`re`**   | Regular expression-based email validation |
| **`csv`**  | Reading and writing CSV files             |

## 🔎 Email Validation Logic

The Regex validates the structure of an email address by checking both the **local part** and **domain part**.

### Local Part

The section before `@`:

* Must start and end with a **letter or digit**
* Can contain:

  * Letters
  * Digits
  * `_`
  * `.`
  * `%`
  * `+`
  * `-`
* Does not allow **consecutive dots**
* Does not allow trailing special characters

### Domain Part

The section after `@`:

* Must start and end with a **letter or digit**
* Can contain hyphens internally
* Must contain at least one `.`
* Requires a **2–4 character domain extension**

Examples:

```text
example@gmail.com
user.name@company.org
student123@college.net
```

## 📊 Input → Processing → Output

```text
          5,000 Row CSV
                │
                ▼
        ┌─────────────────┐
        │  Read CSV Data  │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │  Regex Validator│
        └────────┬────────┘
                 │
          ┌──────┴──────┐
          ▼             ▼
       ✅ Valid       ❌ Invalid
          │             │
          ▼             ▼
   valid_emails.csv  invalid_emails.csv
```

## 📁 Output

The pipeline automatically creates:

```text
valid_emails.csv
invalid_emails.csv
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/aaditya-hamirani07/Email-Validator-Pipeline.git
cd Email-Validator-Pipeline
```

### 2. Run the script

```bash
python email_validator.py
```

### 3. Check the generated files

```text
valid_emails.csv
invalid_emails.csv
```

## 🎯 Purpose

This project demonstrates practical use of:

* Python file handling
* CSV data processing
* Regular expressions
* Data validation
* Basic automation pipelines

---

⭐ **Built with Python** | CSV Processing • Regex • Automation
