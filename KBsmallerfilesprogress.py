import os
import re

# this section should create 12 different output files
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