import cryptography
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

inputPassword = "EncryptionTest"
password = inputPassword.encode()  # convert input -> byte object

# salt the password [is random data that is used as an additional input to a one-way function that "hashes" data,
# a password or passphrase]
# from saltGenerator : b'M\x9bd\xa2e\xc6\x174cKm\xab\xb7\xf7\xae0'
salt = b'M\x9bd\xa2e\xc6\x174cKm\xab\xb7\xf7\xae0'

kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())

key = base64.urlsafe_b64encode(kdf.derive(password))  # kdf used at most 1 time
print(key)
