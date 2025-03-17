import re

def check_password_strength(password):
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(r"[@$!%*?&#]", password))
    }
    
    score = sum(strength_criteria.values())
    
    suggestions = []
    if not strength_criteria["length"]:
        suggestions.append("Increase password length to at least 8 characters.")
    if not strength_criteria["uppercase"]:
        suggestions.append("Add at least one uppercase letter.")
    if not strength_criteria["lowercase"]:
        suggestions.append("Add at least one lowercase letter.")
    if not strength_criteria["digit"]:
        suggestions.append("Include at least one number.")
    if not strength_criteria["special_char"]:
        suggestions.append("Use at least one special character (@$!%*?&#).")
    
    if score == 5:
        return "Strong Password ✅"
    elif score >= 3:
        return "Moderate Password ⚠️\nSuggestions: " + " ".join(suggestions)
    else:
        return "Weak Password ❌\nSuggestions: " + " ".join(suggestions)

if __name__ == "__main__":
    password = input("Enter your password: ")
    print(check_password_strength(password))
