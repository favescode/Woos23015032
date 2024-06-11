import re
email = input("Enter your email address: ")
    # Regular expression for validating email addresses
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Check if the email matches the pattern
if re.match(email_regex, email):
     print("valid email")
else:
    print('not matched to regular email')

# Example usage:
# if email:
#    print("Valid email address.")
# else:
#    print("Invalid email address.")