BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password1 = input("Enter a new password: ")
password2 = input("Re-enter the password: ")
if password1 != password2:
    print("Error: Passwords do not match")
elif not (8 <= len(password1) <= 12):
    print("Error: Password must be 8-12 characters long")
elif password1.lower() in BAD_PASSWORDS:
    print("Error: Password is too common")
else:
    print("Password Set")

