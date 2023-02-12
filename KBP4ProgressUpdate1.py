import re
from os.path import exists 
from urllib.request import urlretrieve 


logtest = 'project3logfile.txt'

if not exists(logtest): 
    print("File not found on system. The log file is being retrieved now.")
    URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    LOCAL_FILE = 'project3logfile.txt'
    local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
    print("The file has been retrieved and saved locally.")
else:
    print("This file is already on your system")

with open(logtest,'r') as fp:
    x = len(fp.readlines())
    print('The total amount of requests in the log file is: ', x)



errorcodes = 0
redirects = 0

openfile = open(logtest)
for line in open(logtest):
    openfile.readline()
    if '403 -' in line:
        errorcodes = errorcodes + 1
    if '404 -' in line:
        errorcodes = errorcodes + 1
    if '304 -' in line:
        redirects = redirects + 1
    if '302 -' in line:
        redirects = redirects + 1

print("Number of errors reported: " + str(errorcodes))
print("Number of redirects reported: " + str(redirects))

