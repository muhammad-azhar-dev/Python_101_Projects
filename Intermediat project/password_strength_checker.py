import re

def check_password_strength(password):
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        suggestions.append("Add at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if re.search(r'[0-9]',password):
        strength += 1
    else:
        suggestions.append("Add at least one digit.")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        suggestions.append("Add at least one special character.")
    
    return strength, suggestions


def main():
    password = input("Enter your password: ")
    strength, suggestions = check_password_strength(password)

    print(f"\nPassword strength: {strength}/5")
    if strength < 5:
        print("suggestions to improve your password: ")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("Your password is strong!")
    

if __name__=="__main__":
    main()
