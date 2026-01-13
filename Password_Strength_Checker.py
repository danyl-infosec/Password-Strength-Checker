# loading of the wordlist
with open("10k-most-common.txt", "r", encoding="latin-1") as file:
    common_passwords = [line.strip() for line in file]

while True:
    password = input("Please enter a password (or type exit to quit): ")
    if password.lower() == "exit":
     break

    score = 0

    has_number = any(char.isdigit() for char in password)
    has_letter = any(char.isalpha() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    # length check
    if len(password) < 8:
        print ("Your password is too short")
    # no points added
    else:
        score += 1

    # variety check
    if has_number and has_letter and has_symbol:
        score += 2
    elif password.isalpha() or password.isdigit():
        print("Your password needs more variety")
        # no points added
    else:
        score += 1

    # wordlist check
    if password in common_passwords:
     score += -2
     print("Your password is too common")

    # Password ratings
    if score <= 0:
     rating = "Weak"
    elif score <= 2:
      rating = "Medium"
    else:
     rating = "Strong"

    print(f"Password Rating: {rating} | Score: {score}")



