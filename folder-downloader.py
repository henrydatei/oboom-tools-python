from oboomAPI import *
from functions import *
from multiprocessing.pool import ThreadPool

data = json.loads(getFolderContent(session, "81GYPMMX"))
fileIDs = []


for file in data[2]:
    fileIDs.append(file['id'])

print(fileIDs)

results = ThreadPool(7).imap_unordered(downloadFileAndSaveToDisk, fileIDs)
for path in results:
    print(path)
