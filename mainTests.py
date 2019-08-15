from cryptography.fernet import Fernet

# 1.key from testKey.key
# 2.encode text
# 3.encrypt text
# 4 decrypt text

# 1
file = open('testKey.key')
key = file.read()  # key : bytes
file.close()

# 2
message = 'Help! A guinea pig tricked me!'
encodedMessage = message.encode()
# print(encodedMessage)

# 3
E = Fernet(key)
encryptedMessage = E.encrypt(encodedMessage)
print(encryptedMessage)

# 4
