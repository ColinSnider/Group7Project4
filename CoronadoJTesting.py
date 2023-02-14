from urllib.request import urlretrieve  

requests = 'project3logfile.txt'
#? This is the correct Url request
url = "https://s3.amazonaws.com/tcmg476/http_access_log"
count = 0

while True: 
    try:
        response = requests.get(url)
        count += 1
        print(f"Number of request made each day: {count}")
    except:
        print("This is the end")
        break