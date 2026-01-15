import random
import string
def hide_message(message):
    interval = random.randint(2, 20)
    encrypted = ""
    for char in message:
        encrypted += char
        for _ in range(interval - 1):
            encrypted += random.choice(string.ascii_letters)
    return encrypted, interval
def reveal_message(encrypted_message, interval):
    return encrypted_message[::interval]
msg = input("Enter a message to encrypt: ")
encrypted_msg, interval_used = hide_message(msg)
print("Encrypted message:", encrypted_msg)
print("Interval used:", interval_used)
decrypted_msg = reveal_message(encrypted_msg, interval_used)
print("Decrypted message:", decrypted_msg)
