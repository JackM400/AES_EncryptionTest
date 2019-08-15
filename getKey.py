from cryptography.fernet import Fernet

file = open('testkey.key', 'rb')
key = file.read()
file.close()
print(key)