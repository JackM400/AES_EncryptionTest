from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
file = open('testkey.key', 'wb')  # file name = testkey
file.write(key)  # file in type bytes
file.close