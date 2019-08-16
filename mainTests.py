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
# 1 open target file
targetFile = open('EncryptedTextSource', "rb")
text = targetFile.read()

encryptText = Fernet(key)
encryptTextMessage = encryptText.encrypt(text)
# write encrypted text to file , this is what would be transmitted
encryptedFile = open("EncryptedTextSource.encrypted", "wb")
encryptedFile.write(encryptTextMessage)

# decrypt target file
targetFile = open("EncryptedTextSource.encrypted", "rb")
encryptiontest3 = targetFile.read()

encrypt_3 = Fernet(key) #TODO find whats rasing InvalidToken
encryptedTextMessage = encryptText.decrypt(encryptiontest3)

file = open("EncryptedTextSource.decrypted", "wb")
file.write(encryptedTextMessage)
