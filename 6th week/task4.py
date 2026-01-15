def encrypt(message):
    message_no_spaces = message.replace(" ", "")
    encrypted_message = message_no_spaces[::-1]
    return encrypted_message
msg = input("Enter a message: ")
print("Encrypted message:", encrypt(msg))

