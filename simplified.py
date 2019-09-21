import cryptography.fernet as set

# TODO
# 1.generate base key ,
# 2.get input message ,
# 3.process message to encrypt ,
# 3a.check encryption ,
# transmit ,
# 4.decrypt message ,
# act -on message

# 1
seed = set.Fernet.generate_key()
key = set.Fernet(seed)

# 2
targetFile = open('simplified_text', "r")
text = targetFile.read()
print(text)
