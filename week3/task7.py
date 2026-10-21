
import string


def check_minimum_length(password, min_length=8):
    return len(password) >= min_length


def check_uppercase(password):
    return any(char.isupper() for char in password)


def check_lowercase(password):
    return any(char.islower() for char in password)


def check_digits(password):
    return any(char.isdigit() for char in password)


def check_special_characters(password):
    return any(char in string.punctuation for char in password)


def analyze_password(password, min_length=8):
    checks = {
        "Minimum length": check_minimum_length(password, min_length),
        "Uppercase letters": check_uppercase(password),
        "Lowercase letters": check_lowercase(password),
        "Digits": check_digits(password),
        "Special characters": check_special_characters(password)
    }

    missing = [
        requirement
        for requirement, passed in checks.items()
        if not passed
    ]

    return {
        "password_length": len(password),
        "checks": checks,
        "missing_requirements": missing,
        "valid": all(checks.values())
    }


password = input("Enter the password: ")

print( analyze_password(password))