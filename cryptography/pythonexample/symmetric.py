#!/usr/bin/env python3

import os
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()

# Generate Key and Initialization Vector (IV)
key = os.urandom(32)
iv = os.urandom(16) # This is not used in AES-ECB mode

message = b"Cryptography in Network Security" 
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

