import cryptography.fernet as process

# 1.Generate Base Key
seed = process.Fernet.generate_key()
key = process.Fernet(seed)

# 2.Get Input Message
targetFile = open('simplified_text', "r")
text = targetFile.read()

print("Message to Encrypt :\n" + text)

# 3.Process Message To Encrypt
b_text: bytes = str.encode(text)
encrypted_message = key.encrypt(b_text)
print(encrypted_message)  # 3a.Check Encryption

#
#   Transmit Message
#

# 4.Decrypt Message
decrypted_message = key.decrypt(encrypted_message)  # Message (Byte Form)
print(decrypted_message)  # 4a.Check Decryption

#
#   Act-on Message
#

# Programme End
