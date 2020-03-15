import requests

def login(username, passwordhash):
    parameters = {"auth": username, "pass": passwordhash, "source": 1}
    req = requests.get('https://www.oboom.com/1/login', params=parameters)
    req.raise_for_status()
    return req.text

def setPincode(session, pin):
    parameters = {"token": session, "pin": pin}
    req = requests.get('https://www.oboom.com/1/pincode/set', params=parameters)
    req.raise_for_status()
    return req.text

def isPincode(session):
    parameters = {"token": session}
    req = requests.get('https://www.oboom.com/1/pincode/is', params=parameters)
    req.raise_for_status()
    return req.text

def getSecurityToken(session, pin):
    parameters = {"token": session, "pin": pin}
    req = requests.get('https://www.oboom.com/1/pincode/check', params=parameters)
    req.raise_for_status()
    return req.text

def getFileInformation(session, itemID):
    parameters = {"token": session, "items": itemID}
    req = requests.get('https://api.oboom.com/1/info', params=parameters)
    req.raise_for_status()
    return req.text

def getFileTree(session):
    parameters = {"token": session}
    req = requests.get('https://api.oboom.com/1/tree', params=parameters)
    req.raise_for_status()
    return req.text

def getFolderContent(session, folderID):
    parameters = {"token": session, "item": folderID}
    req = requests.get('https://api.oboom.com/1/ls', params=parameters)
    req.raise_for_status()
    return req.text

def getDiskUsage(session):
    parameters = {"token": session}
    req = requests.get('https://api.oboom.com/1/du', params=parameters)
    req.raise_for_status()
    return req.text

def createFolder(session, parentFolderID, name):
    parameters = {"token": session, "parent": parentFolderID, "name": name}
    req = requests.get('https://api.oboom.com/1/mkdir', params=parameters)
    req.raise_for_status()
    return req.text

def copyFile(session, fileID, targetFolderID, newName):
    parameters = {"token": session, "items": fileID, "target": targetFolderID, "new_name": newName}
    req = requests.get('https://api.oboom.com/1/cp', params=parameters)
    req.raise_for_status()
    return req.text

def moveFile(session, fileID, targetFolderID, newName):
    parameters = {"token": session, "items": fileID, "target": targetFolderID, "new_name": newName}
    req = requests.get('https://api.oboom.com/1/mv', params=parameters)
    req.raise_for_status()
    return req.text

def removeFile(session, fileID, recursive='true', moveToTrash='true'):
    parameters = {"token": session, "items": fileID, "recursive": recursive, "move_to_trash": moveToTrash}
    req = requests.get('https://api.oboom.com/1/rm', params=parameters)
    req.raise_for_status()
    return req.text

def createDownloadTicket(session, fileID):
    parameters = {"token": session, "item": fileID}
    req = requests.get('https://api.oboom.com/1/dl', params=parameters)
    req.raise_for_status()
    return req.text

def downloadFile(domain, ticket):
    parameters = {"ticket": ticket}
    req = requests.get('https://{}/1/dlh'.format(domain), params=parameters)
    req.raise_for_status()
    return req.content

def addRemoteUpload(session, url, folderID):
    link = "https://api.oboom.com/1/remote/add?token=" + str(session) + "&remotes=[{\"url\": \"" + str(url) + "\", \"parent\": \"" + str(folderID) + "\"}]"
    req = requests.get(link)
    req.raise_for_status()
    return req.text

def removeRemoteUpload(session, uploadJobID):
    parameters = {"token": session, "remotes": uploadJobID}
    req = requests.get('https://api.oboom.com/1/remote/rm', params=parameters)
    req.raise_for_status()
    return req.text

def getAllRemoteUploads(session):
    parameters = {"token": session}
    req = requests.get('https://api.oboom.com/1/remote/lsall', params=parameters)
    req.raise_for_status()
    return req.text
