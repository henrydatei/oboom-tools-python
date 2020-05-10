from oboomAPI import *
import hashlib
import binascii
import json
import os.path

def getSession(username, password):
    passwordhashBytes = hashlib.pbkdf2_hmac('sha1', password.encode(), password[::-1].encode(), 1000, 16)
    passwordhash = binascii.hexlify(passwordhashBytes).decode()
    JSON = json.loads(login(username, passwordhash))
    session = JSON[1]['session']
    return session

file = open("account.txt", "r")
logindata = file.read().splitlines()
username = logindata[0]
password = logindata[1]
session = getSession(username, password)

def downloadFileAndSaveToDisk(fileID):
    downloadInfos = json.loads(createDownloadTicket(session, fileID))
    server = downloadInfos[1]
    ticket = downloadInfos[2]
    infos = json.loads(getFileInformation(session, fileID))
    name = infos[1][0]['name']
    
    if os.path.exists(name):
        print('Skipping: File already downloaded: ' + name)
    
    else:
        filedata = downloadFile(server, ticket)
        if filedata == '[503,"download"]':
            print('Error for ' + name)
        else:
            f = open(name, "wb")
            f.write(filedata)
            print('File successfully downloaded: ' + name)
    
