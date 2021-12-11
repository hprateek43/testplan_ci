import sys
import time
import requests
import random

print(sys.argv[1])

time.sleep(30)

with open('results.csv',"w+") as f:
    f.write("Avg,Median,90,min,max,samples,errors,error %")
    line = str(random.uniform(500.00,530.00))+","+str(random.uniform(150.00,230.00))+","+str(random.uniform(900.00,1300.00))+","+str(random.uniform(0.500,3.00))+","+"16550,97560,360,0.37"
    f.write(line)

requests.post(
    url=sys.argv[1],
    data={
        "status":"OK",
        "path":"D:\res"
    }
)