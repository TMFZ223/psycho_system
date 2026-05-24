import re
import random
import string

activation_storage = {}

def validate_email(email):
    if not email:
        return "email should not be empty"
    if "@" not in email or "." not in email:
        return "email should be an email"

def validate_password(password):
    if not password:
        return "password should not be empty"
    if len(password) < 7 or len(password) > 30:
        return "Password must be between 7 and 30 characters"
    if re.search(r"\s", password) or re.search(r"[а-яА-Я]", password):
        return "invalid format of password"

def generate_code():
    return ''.join(random.choices(string.digits, k=6))