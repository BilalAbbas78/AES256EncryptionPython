from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
import os

# Padding for the input string --not
# related to encryption itself.
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

# Random 256-bit key
random_key = os.urandom(32)


class AESCipher:
    """
    Usage:
        c = AESCipher('password').encrypt('message')
        m = AESCipher('password').decrypt(c)
    Tested under Python 3 and PyCrypto 2.6.1.
    """

    def __init__(self, key):
        self.key = md5(key).hexdigest()

    def encrypt(self, raw):
        raw = pad(raw)
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        return b64encode(cipher.encrypt(raw.encode('utf8')))

    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        return unpad(cipher.decrypt(enc)).decode('utf8')


# MAIN
# msg = input('Message...: ')
# # pwd = input('Password..: ')
#
# cipherText = AESCipher(random_key).encrypt(msg)
# print(random_key)
#
# print(cipherText)
#
# decipher = AESCipher(random_key).decrypt(cipherText)
#
# print(decipher)
# # print('Ciphertext:', AESCipher(pwd).encrypt(msg))
# # print('Ciphertext:', AESCipher(pwd).decrypt(msg))

fileRead = open("C:\\Users\\Syed Bilal Abbas\\Desktop\\test.txt", "r")
fileWrite = open("C:\\Users\\Syed Bilal Abbas\\Desktop\\myfile.txt", "w+")

# print(f.readline())

# reading each line
for line in fileRead:

    # reading each word
    for word in line.split():
        # displaying the words
        # print(word)
        fileWrite.write(AESCipher(random_key).encrypt(word).decode("utf-8") + " ")
    fileWrite.write("\n")

fileWrite.close()

print("Reading encrypted file")
fileRead = open("C:\\Users\\Syed Bilal Abbas\\Desktop\\myfile.txt", "r")
for line in fileRead:
    for word in line.split():
        # print(word)
        print(AESCipher(random_key).decrypt(word.encode("utf-8")) + " ", end='')
    print()

fileWrite.close()