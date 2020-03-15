from oboomAPI import *
import hashlib
import binascii
import json

def getSession(username, password):
    passwordhashBytes = hashlib.pbkdf2_hmac('sha1', password.encode(), password[::-1].encode(), 1000, 16)
    passwordhash = binascii.hexlify(passwordhashBytes).decode()
    JSON = json.loads(login(username, passwordhash))
    session = JSON[1]['session']
    return session
