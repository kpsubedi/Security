
""" Symmetric Cryptography Problem 

In this problem you will use modes of AES Symmetric algorithm to encrypt and decrypt the messages. AES supportes 
different modes of operation: ECB, CBC, CTR.

Problems:
1. We will use AES-CBC mode to perform encryption and decryption of the input data.
2. We will use AES-CTR mode to perform encryption and decryption of the input data.

ECB mode of operation example is here: https://github.com/kpsubedi/Security/blob/master/cryptography/pythonexample/symmetric_demo.py

To solve these problmes, you need to go through the api documentation here: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#cryptography.hazmat.primitives.ciphers.Cipher
"""

### Problem 1 ###


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()

# Initialize key and initialization vector using urandom() form os package.
import os

key = os.urandom(32)
iv = os.urandom(16)

# Complete the following code to complete the CBC mode of operation in AES


