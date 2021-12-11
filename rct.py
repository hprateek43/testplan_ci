import sys
import time
import requests
import random
import datetime
print(sys.argv[1])


with open('results.csv',"w+") as f:
    f.write("timestamp,min,max,average")
    i=0
    while(i<50):
        line = str(datetime.datetime.now())+","+str(random.uniform(80.00,85.00))+","+str(random.uniform(85.00,90.00))+","+str(random.uniform(82,87))+"\n"
        f.write(line)
        time.sleep(1)
        i = i+1

requests.post(
    url=sys.argv[1],
    data={
        "status":"OK",
        "path":"D:\res"
    }
)