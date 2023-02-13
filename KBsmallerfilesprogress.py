import os
from collections import defaultdict
from datetime import date, datetime
from os.path import exists

with open("project3logfile.txt", "r") as f:
    log_lines = f.readlines()
    month_lines = defaultdict(list)

    for line in log_lines:
        # line below this (12) is giving me a hard time with "time data "local" does not match format, nothing else appears to give errors but I'm having a hard time checking
        date_str = datetime.strptime(line.split()[0], '%d/%b/%Y:%H:%M:%S %z')
        # line below this is test code I dont want to get rid of yet
        #date = datetime.strptime(date_str, '%d/%m/%Y:%H:%M:%S')
        month = date.month

        month_lines[month].append(line)

    for month, lines in month_lines.items():
        filename = "logfile_{}.txt".format(month)
        with open(filename, "w") as f:
            f.writelines(lines)

# Messed around with having it say if the files are saved or not, very rushed code that doesnt work but wanted to throw it in to see if anyone can figure it out in the meantime
if not exists(filename): 
    print("Files not found on system. The log file is being split now.")
else:
    print("These files are already on your system")