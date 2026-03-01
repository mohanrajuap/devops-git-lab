import requests
import time
import json
url = "https://api.github.com/users/octocat"
for i in range(1,4):
    try:
      response=requests.get(url, timeout=5)
      if response.status_code==200:
       data=response.json()
       print(data.get("login"))
       print(data.get("followers"))
       print(data.get("following"))
       break
      else:
        print("Getting response is failed in attempt",i)
    except requests.exceptions.Timeout:
     print("timeout happened")
     time.sleep(2)
else:
  print("API UNAVAILABLE – ESCALATE TO L2")