import re
from os.path import exists 
from urllib.request import urlretrieve 
from collections import defaultdict


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


#Sunjeeth and Juan contribution, commented out the code due to errors
#? This is the correct Url request
#url = "https://s3.amazonaws.com/tcmg476/http_access_log"



#filename = "log_file_local.txt"

#def download_local_copy():
    #f=open(filename,"a")

    #with requests.get(url,stream=True) as r_open:
        #f.write(r_open.text)

    #f.close()


#if not os.path.isfile(filename):
    #download_local_copy()


#lines = []
#with open(filename,"r") as f:
    #lines = f.readlines()


#dct = defaultdict(int)


#local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150

#'''
#SOME LINES DO NOT HAVE The DATE
#'''
#for line in lines:
    #parsed_out_date = line.split(' ')[3].split(':')[0].strip('[]')
    #dct[parsed_out_date]+=1

#print(dct)


#Colin Contribution, #2
requests = 'project3logfile.txt'
#? This is the correct Url request
url = "https://s3.amazonaws.com/tcmg476/http_access_log"
count = 0

while True: 
    try:
        response = requests.get(url)
        count += 1
        print(f"Number of request made each Week: {count}")
    except:
        print("This is the end")
        break

while True: 
    try:
        response = requests.get(url)
        count += 1
        print(f"Number of request made each Month: {count}")
    except:
        print("This is the end")
        break


# 3 and 4 below this, Keller contribution
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


z = float(errorcodes)/float(x)
zz = float(redirects)/float(x)

print("Number of errors reported: " + str(errorcodes))
print("Number of redirects reported: " + str(redirects))
print("Number of errors reported in percentage form is: " + str(z*100) + ' %')
print("Number of redirects reported in percentage form is: " + str(zz*100)+ ' %')

#Vivianna Contribution, #5 and 6
fnames = {}

with open('project3logfile.txt') as rec:
    L = rec.readlines()
    for line in L: 
        reqfiles = re.split("[A-Z]{3} (.+) HTTP/1.0", line) #pattern
        
        if len(reqfiles) == 3:
            file = reqfiles[1]
        
        if file in fnames:
            fnames[file] += 1
        else: 
            fnames[file] = 1

print("Most requested: " + str(list(fnames.keys())[0])) 
print("Least requested: " + str(list(fnames.keys())[-1]))

#Dylans COntribution
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
output_files = {}
for month in months:
    output_files[month] = open(f"{month}_log.txt", "w")

# this section opens the input log file and read the content inside, extract the month, then write the line to the right output file
with open("project3logfile.txt", "r") as input_file:
    for line in input_file:        
        month_match = re.search(r"\[(\d{2})/(\w{3})/\d{4}", line)
        if month_match:
            month = month_match.group(2)
            output_files[month].write(line)

# This section will close all output files
for output_file in output_files.values():
    output_file.close()