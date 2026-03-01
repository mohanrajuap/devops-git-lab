
from pathlib import Path
import requests
Path_1=Path("C:/Users/raju2/OneDrive/Documents/py/status.log")
url="https://api.github.com/users/octocat"
resp=requests.get(url,timeout=5)
if resp.status_code != 200:
    with Path_1.open('w') as v:
        v.write("API is down")
else:
    print("API is fine")