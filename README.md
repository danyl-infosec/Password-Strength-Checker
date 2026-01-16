# Password-Strength-Checker
A Python-based password checker that analyzes password strength and uniqueness, testing against the SecLists 10k-most-common wordlist to help users create stronger, safer credentials.

Created by **Danyl Morris** — my first professional project in Python.  
This tool analyzes passwords for uniqueness and overall strength, testing them against the `10k-most-common.txt` wordlist from [SecLists](https://github.com/danielmiessler/SecLists).  
The script can scale to larger wordlists if needed. 

---

## Why Strong Passwords Matter

The need for strong passwords cannot be overstated.  
In our modern world, cybercriminals can crack vast password lists at lightning speed, testing millions of combinations within minutes.  
This gives them the ability to:
- Gain access to and steal personal data
- Steal identities
- Drain financial accounts
... to name just a few of the potential consequences 

Luckily, we don’t have to be like lambs to the slaughter.  
We can take steps to protect ourselves against these bad actors by creating strong passwords.

---

## What Makes a Password Strong?

- At least **8 characters long**  
- Includes a mix of **letters, numbers, and symbols**  
- Screened against lists of **common/breached passwords** to ensure it isn’t already compromised

---

## Project Goal

The password checker I have created aims to help everyday internet users do just this:  
create stronger, safer credentials and reduce their risk of compromise.

---

## Features

- ✅ Length check (minimum 8 characters)  
- ✅ Variety check (letters, numbers, symbols)  
- ✅ Wordlist check (against 10k-most-common.txt)  
- ✅ Interactive loop (test multiple passwords until you type "exit")  
- ✅ Scoring system with ratings: Weak, Medium, Strong

---

## Scoring System

- **Weak**: Score ≤ 0  
- **Medium**: Score = 1 or 2  
- **Strong**: Score = 3  

The maximum score is 3, based on:
- +1 for meeting minimum length (≥ 8 characters)  
- +2 for including letters, numbers, and symbols  
- −2 penalty if found in the common password list

---

## Usage

Clone the repository and run:

```bash
python password_strength_checker.py
```

---

## Wordlist Requirement

This project uses the [`10k-most-common.txt`](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt) file from the [SecLists](https://github.com/danielmiessler/SecLists) repository.  

To enable the wordlist check:
1. Download the file from SecLists.
2. Place it in the same folder as `password_strength_checker.py`.
3. Run the script as described in the Usage section.

Without the wordlist, the script will still run, but only length and character variety checks will be applied.
