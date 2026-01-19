def validate_password(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    special_chars = "!@#$%^&*"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    if has_upper and has_lower and has_digit and has_special:
        return True
    return False

password = input("Enter a strong password:")
if validate_password(password):
    print("Strong password")
else:
    print("Weak password")

