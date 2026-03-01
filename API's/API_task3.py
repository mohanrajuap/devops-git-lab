import requests
import json
import time
url="https://api.github.com/users/octocat"
for i in range(1,4):
    try:
        response=requests.get(url,timeout=5)
        if response.status_code==200:
         print("LOGIN WORKING")
         break
    except requests.exceptions.Timeout:
      print("FAILED")