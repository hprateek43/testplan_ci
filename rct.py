import sys
import time
import requests

print(sys.argv[1])

time.sleep(30)

requests.post(
    url=sys.argv[1],
    data={
        "status":"OK",
        "path":"D:\res"
    }
)