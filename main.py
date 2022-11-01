from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
import os
import time
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = 16  # Bytes

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
        raw = pad(raw, BLOCK_SIZE)
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        return b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        return unpad(cipher.decrypt(enc), BLOCK_SIZE).decode('utf8')


# MAIN
start = time.time()

fileRead = open("C:\\Users\\Syed Bilal Abbas\\Desktop\\test2.txt", "r", encoding="utf8")
fileWrite = open("C:\\Users\\Syed Bilal Abbas\\Desktop\\myfile.txt", "w+", encoding="utf8")

# reading each line
for line in fileRead:

    # reading each word
    for word in line.split():
        # displaying the words
        # print(word)
        fileWrite.write(AESCipher(random_key).encrypt(word.encode("utf8")).decode("utf8") + " ")
    fileWrite.write("\n")

fileWrite.close()

end = time.time()
print("Encryption time: %.2f seconds" % round(end - start, 2))

print("Reading encrypted file:\n")
fileRead = open("C:\\Users\\Syed Bilal Abbas\\Desktop\\myfile.txt", "r", encoding="utf8")
for line in fileRead:
    for word in line.split():
        # print(word)
        print(AESCipher(random_key).decrypt(word.encode("utf8")) + " ", end='')
    print()

fileWrite.close()
