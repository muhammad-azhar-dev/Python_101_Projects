# windows : C:\Windows\System32\drivers\etc
# linux && mac : etc\hosts
import time 
from datetime import datetime as dt
host = 'D:\\udemy\\my records for udemy\\python alpha + course\\app2 website blocker\\files\hosts'

host_path = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com','facebook.com','www.google.com','www.youtube.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,1) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print('work hour....')
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ ' '+website+'\n' )
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("not work time ....")
    # print('hello') 
    time.sleep(5)