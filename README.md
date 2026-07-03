Email Validator Pipeline

A quick automation script that take , 5000 row CSV dataset , filters valid email and invalid email using Regex and autosorts into respective csv files

Tech Stack 
Language : Python
Modules : re and csv

This regex checks if an email is valid.

This regex is designed to validate email addresses

It ensures the local part (before @) starts and ends with a letter or digit, and may contain letters, digits, underscores, dots, %, +, or - inside, but it does not allow consecutive dots or trailing symbols. The domain part (after @) must also start and end with a letter or digit, can include hyphens inside but not at the edges, and must contain at least one dot followed by 2–4 letters to represent a valid domain such as .com, .org, or .net.