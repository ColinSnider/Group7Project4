import requests
from collections import defaultdict
import os 
#? This is the correct Url request
url = "https://s3.amazonaws.com/tcmg476/http_access_log"



filename = "log_file_local.txt"

def download_local_copy():
    f=open(filename,"a")

    with requests.get(url,stream=True) as r_open:
        f.write(r_open.text)

    f.close()


if not os.path.isfile(filename):
    download_local_copy()


lines = []
with open(filename,"r") as f:
    lines = f.readlines()


dct = defaultdict(int)


#local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150

'''
SOME LINES DO NOT HAVE The DATE

'''
for line in lines:
    parsed_out_date = line.split(' ')[3].split(':')[0].strip('[]')
    dct[parsed_out_date]+=1

print(dct)