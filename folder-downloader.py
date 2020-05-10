from oboomAPI import *
from functions import *
from multiprocessing.pool import ThreadPool

folderID = input("FolderID: ")
threads = input("Threads: ")

data = json.loads(getFolderContent(session, folderID))
fileIDs = []

for file in data[2]:
    fileIDs.append(file['id'])

print(fileIDs)

results = ThreadPool(int(threads)).imap_unordered(downloadFileAndSaveToDisk, fileIDs)