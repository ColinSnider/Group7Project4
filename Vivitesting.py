import re
from os.path import exists 
from urllib.request import urlretrieve 

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
