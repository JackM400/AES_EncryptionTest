import cryptography.fernet as process

#TODO
# 1.generate base key ,
# 2.get input message ,
# 3.process message to encrypt ,
# 3a.check encryption ,
# transmit ,
# 4.decrypt message ,
# act -on message

# 1
seed = process.Fernet.generate_key()
key = process.Fernet(seed)

# 2
targetFile = open('simplified_text', "r")
text = targetFile.read()
print("Message to Encrypt :\n" + text)
b_text = str.encode(text)

# 3
encrypted_message = key.encrypt(b_text)
print(encrypted_message)
