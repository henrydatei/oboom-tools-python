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

def downloadFileAndSaveToDisk(session, fileID):
    downloadInfos = json.loads(createDownloadTicket(session, fileID))
    server = downloadInfos[1]
    ticket = downloadInfos[2]
    infos = json.loads(getFileInformation(session, fileID))
    name = infos[1][0]['name']

    f = open(name, "w+")
    filedata = downloadFile(server, ticket)
    f.write(filedata)
