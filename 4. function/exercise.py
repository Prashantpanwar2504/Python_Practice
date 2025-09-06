# password strength checker
# Requirement for Strong Password
# length > 8
# should contain at-least 1 digit
# should contain at-least one lower case character.
# should contain at-least in upper case character
# should contain atleast one spacial character "!@#$%^&*()_+".

def check_password_strength(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in "!@#$%^&*()_+" for char in password):
        return False
    else:
        return True


password = input("Enter a Strong Password:")

result = check_password_strength(password)

if result == False:
    print("Password is weak.")
else:
    print("Password is Strong.")