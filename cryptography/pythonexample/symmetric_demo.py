#!/usr/bin/env python3

import os
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()

# Generate Key and Initialization Vector (IV)
key = os.urandom(32)
iv = os.urandom(16) # This is not used in AES-ECB mode

message = b"Cloud Security 2023 Spring - CBU"  # Task 1
print("Original Message: %s" %(message))

algorithm = algorithms.AES(key)
cipher_ecb = Cipher(algorithm, mode=modes.ECB(), backend=backend)

# Encryption 
encryptor = cipher_ecb.encryptor()
ct = encryptor.update(message) + encryptor.finalize()

print("Cipher Test: %s" %(ct))

# Decryption
decryptor = cipher_ecb.decryptor()
pt = decryptor.update(ct) + decryptor.finalize()

print("Decrypted Message: %s" %(pt))

#######################################################################################
#!/usr/bin/env python3
import random
import string

import os
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()

# Generate Key and Initialization Vector (IV)
key = os.urandom(32)
iv = os.urandom(16)

# 

mytext = b"Welcome to Cloud Security 2023 Spring - CBU"
print("Original Message: %s" %(mytext))

print(key)
print(iv)

cipher_cbc = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher_cbc.encryptor()
# print(type(mytext))

# key track of how many bytes padded to make multile of 16 bytes
count = 0
while len(mytext) % 16 != 0:
    mytext = mytext + bytes(random.choice(string.ascii_letters), encoding='utf-8')
    count = count + 1

print(count)

ct = encryptor.update(mytext) + encryptor.finalize()
print(ct)


decryptor = cipher_cbc.decryptor()
pt = decryptor.update(ct)
print(pt[0:len(pt)-count])
###########################################################################
