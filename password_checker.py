import re
def check_password_strength(password):
    strength = 0
    feedback = []
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append(" Use at least 8 characters.")
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append(" Add lowercase letters.")
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append(" Add uppercase letters.")
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include numbers.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include special characters.")
    if strength <= 2:
        result = "Weak Password"
    elif strength == 3 or strength == 4:
        result = "Moderate Password"
    else:
        result = "Strong Password"
    return result, feedback
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result, tips = check_password_strength(pwd)
    print("\nPassword Strength:", result)
    if tips:
        print("Suggestions:")
        for tip in tips:
            print(tip)
