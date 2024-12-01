import secrets
import string

def generate_password(length, use_letters, use_digits, use_punctuation, min_letters, min_digits, min_punctuation):
    if length < (min_letters + min_digits + min_punctuation):
        return "Password length should be at least the sum of minimum counts for each character type."

    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        return "No character types selected."

    password = []
    if use_letters and min_letters > 0:
        password += [secrets.choice(string.ascii_letters) for _ in range(min_letters)]
    if use_digits and min_digits > 0:
        password += [secrets.choice(string.digits) for _ in range(min_digits)]
    if use_punctuation and min_punctuation > 0:
        password += [secrets.choice(string.punctuation) for _ in range(min_punctuation)]

    password += [secrets.choice(characters) for _ in range(length - len(password))]
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def update_strength_indicator(password, strength_label):
    length = len(password)
    has_letters = any(c.isalpha() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_punctuation = any(c in string.punctuation for c in password)

    strength = "Weak"
    if length >= 8 and has_letters and has_digits and has_punctuation:
        strength = "Strong"
    elif length >= 6 and ((has_letters and has_digits) or (has_letters and has_punctuation) or (has_digits and has_punctuation)):
        strength = "Medium"

    strength_label.config(text=f"Password Strength: {strength}")
