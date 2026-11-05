import string

# Common passwords to flag
common_passwords = [
    "password",
    "password123",
    "12345678",
    "qwerty123",
    "admin123"
]

password = input("Enter a sample password to check: ")

score = 0
feedback = []

# Check whether the password is common
if password.lower() in common_passwords:
    print("\nWARNING: This is a commonly used password!")
    score = 0
    feedback.append("Choose a less predictable password.")
else:
    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add a special character.")

# Display report
print("\n===== PASSWORD SECURITY REPORT =====")
print(f"Basic checks passed: {score}/5")

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Moderate")
else:
    print("Strength: Strong")

if feedback:
    print("\nRecommendations:")
    for item in feedback:
        print("-", item)
else:
    print("\nAll five basic checks passed!")

print("\nNote: This is an educational checker, not a guarantee of password security.")

