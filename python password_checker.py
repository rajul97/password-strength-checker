import re
import random
import string
import time

def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + "@$!%*?&#"
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    print("\n🔍 Analyzing your password strength... Please wait!")
    for dot in "....":
        print(dot, end="", flush=True)
        time.sleep(0.5)
    print("\n")

    # Define strength criteria with descriptive titles
    criteria = {
        "Length (>=12 characters)": len(password) >= 12,
        "At least one uppercase letter": bool(re.search(r"[A-Z]", password)),
        "At least one lowercase letter": bool(re.search(r"[a-z]", password)),
        "At least one digit": bool(re.search(r"\d", password)),
        "At least one special character (@$!%*?&#)": bool(re.search(r"[@$!%*?&#]", password))
    }
    
    # Display the results with a fun, cartoonish style
    for crit, passed in criteria.items():
        status = "✅" if passed else "❌"
        print(f"{status} {crit}")
        time.sleep(0.5)
    
    score = sum(criteria.values())
    suggestions = []
    
    # Prepare specific suggestions for missing criteria
    if not criteria["Length (>=12 characters)"]:
        suggestions.append("Increase the length to at least 12 characters.")
    if not criteria["At least one uppercase letter"]:
        suggestions.append("Add at least one uppercase letter (e.g., A, B, C).")
    if not criteria["At least one lowercase letter"]:
        suggestions.append("Include at least one lowercase letter (e.g., a, b, c).")
    if not criteria["At least one digit"]:
        suggestions.append("Insert at least one number (0-9).")
    if not criteria["At least one special character (@$!%*?&#)"]:
        suggestions.append("Use at least one special character (@, $, !, %, *, ?, &, #).")
    
    # Decide on overall strength and feedback message
    if score == 5:
        strength_msg = "\n🎉 Wow! Your password is SUPER STRONG! 🚀"
        advice = "Keep rocking that secure password! 💪"
    elif score >= 3:
        strength_msg = "\n⚠️ Your password is MODERATE. It can be even better! 😎"
        advice = "Consider these improvements:\n" + "\n".join(suggestions)
    else:
        strength_msg = "\n❌ Oops! Your password is WEAK. Time to level up! 😱"
        advice = "Here are some tips to improve it:\n" + "\n".join(suggestions)
    
    # Generate three strong password suggestions
    strong_options = [generate_strong_password() for _ in range(3)]
    suggestion_msg = "\n💡 Here are three strong password options you might like:\n"
    for idx, pwd in enumerate(strong_options, start=1):
        suggestion_msg += f"   Option {idx}: {pwd}\n"
    
    final_message = (
        strength_msg + "\n" +
        advice + "\n" +
        suggestion_msg + "\n" +
        "🔒 Pro tip: Always use unique passwords for different applications to stay secure!"
    )
    
    return final_message

def main():
    print("✨ Welcome to the Ultimate Cartoonish Password Strength Checker! ✨\n")
    password = input("🔐 Please enter your password: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
