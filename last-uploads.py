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
    url = upload['url']
    if state == 'complete':
        name = upload['name']
        size = upload['size']
        item = upload['item']
        print(bcolors.green + str(state) + bcolors.endColor + " " + str(name) + " (" + str(item) + "), size: " + str(size) + ", url: " + bcolors.blue + str(url) + bcolors.endColor)
    if state == 'pending' or state == 'working':
        loadedSize = upload['loaded_size']
        speed = upload['speed']
        print(bcolors.yellow + str(state) + bcolors.endColor + ", loaded size: " + str(loadedSize) + ", speed: " + str(speed) + ", url: " + bcolors.blue + str(url) + bcolors.endColor)
    if state == 'failed' or state == 'retry':
        loadedSize = upload['loaded_size']
        lastError = upload['last_error']
        print(bcolors.red + str(state) + bcolors.endColor + ", error: " + str(lastError) + ", loaded size: " + str(loadedSize) + ", url: " + bcolors.blue + str(url) + bcolors.endColor)
