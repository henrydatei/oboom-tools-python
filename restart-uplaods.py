from oboomAPI import *
from functions import *
from colors import *

file = open("account.txt", "r")
logindata = file.read().splitlines()
username = logindata[0]
password = logindata[1]
session = getSession(username, password)

lastUploads = json.loads(getAllRemoteUploads(session))

for upload in lastUploads[3]:
    state = upload['state']
    if state == 'failed' or state == 'retry':
        url = upload['url']
        id = upload['id']
        parent = upload['parent']
        print("Resatrting url " + bcolors.blue + str(url) + bcolors.endColor + ", id: " + str(id) + ", parent: " + str(parent))
        removeRemoteUpload(session, id)
        addRemoteUpload(session, url, parent)
