from cryptography.fernet import Fernet

# string encryption + decryption
# 1.key from testKey.key
# 2.encode text
# 3.encrypt text
# 4.decrypt text : encrypted message + key => original
# 5. convert bytes to string

# 1
file = open('testKey.key')
key = file.read()  # key : bytes
file.close()

# 2
message = 'Help! A guinea pig tricked me!'
encodedMessage = message.encode()
# print(encodedMessage)

# 3
encrypt = Fernet(key)
encryptedMessage = encrypt.encrypt(encodedMessage)
print(encryptedMessage)
# print("\n")

# 4
# 4.1 get key
file = open('testkey.key', "rb")
newKey = file.read()  # key : bytes | should be same key as in 1
file.close()
# 4.2 decrypt encrypted message
encrypt_2 = Fernet(key)
decryptedMessage = encrypt_2.decrypt(encryptedMessage)

print(decryptedMessage)  # still :bytes

# 5
originalMessage = decryptedMessage.decode()
print(originalMessage)

# file encryption + decryption

