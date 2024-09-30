from validator_collection import validators

email_address= input("What's your email address?: ")
try:
    valid_email= validators.email(email_address)
    print("Valid")
except:
    print("Invalid")
