BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    password1 = input("Enter a new password: ")
    password2 = input("Re-enter the password: ")
    if password1 != password2:
        print("Error: Passwords do not match\n")
    elif not (8 <= len(password1) <= 12):
        print("Error: Password must be 8-12 characters long\n")
    elif password1.lower() in BAD_PASSWORDS:
        print("Error: Password is too common\n")
    else:
        print("Password Set")
        break
