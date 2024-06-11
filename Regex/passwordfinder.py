# import re

# def check_password_strength(password):
#     # Regular expressions to check for password strength factors
#     length_regex = r'.{8,}'
#     uppercase_regex = r'[A-Z]'
#     lowercase_regex = r'[a-z]'
#     digit_regex = r'\d'
#     special_char_regex = r'[!@#$%^&*()-+=.]'

#     # Check password length
#     if not re.search(length_regex, password):
#         return "Password should be at least 8 characters long."

#     # Check for uppercase letters
#     if not re.search(uppercase_regex, password):
#         return "Password should contain at least one uppercase letter."

#     # Check for lowercase letters
#     if not re.search(lowercase_regex, password):
#         return "Password should contain at least one lowercase letter."

#     # Check for digits
#     if not re.search(digit_regex, password):
#         return "Password should contain at least one digit."

#     # Check for special characters
#     if not re.search(special_char_regex, password):
#         return "Password should contain at least one special character."

#     return "Password is strong!"

# # Example usage:
# password = input("Enter your password: ")
# strength_result = check_password_strength(password)
# print(strength_result)

import re

    # Regular expressions to check for password strength factors
length_regex = r'.{8,}'
uppercase_regex = r'[A-Z]'
lowercase_regex = r'[a-z]'
digit_regex = r'\d'
special_char_regex = r'[!@#$%^&*()-+=.]'
password = input("Enter your password: ")

# Check password length
if not re.search(length_regex, password):
    print ("Password should be at least 8 characters long.")

# Check for uppercase letters
if not re.search(uppercase_regex, password):
    print ("Password should contain at least one uppercase letter.")

# Check for lowercase letters
if not re.search(lowercase_regex, password):
    print ("Password should contain at least one lowercase letter.")

# Check for digits
if not re.search(digit_regex, password):
    print ("Password should contain at least one digit.")

# Check for special characters
if not re.search(special_char_regex, password):
    print("Password should contain at least one special character.")
print("Password is strong!")

# Example usage:
strength_result = password
print(strength_result)

