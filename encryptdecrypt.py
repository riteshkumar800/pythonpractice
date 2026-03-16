import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

print("chars :", chars)
print("key   :", key)

# ENCRYPT
plain_text = input("\nEnter message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print("Encrypted message:", cipher_text)


# DECRYPT
cipher_text = input("\nEnter message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print("Decrypted message:", plain_text)
