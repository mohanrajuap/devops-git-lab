import requests
url="https://api.github.com/users/octocat"
response=requests.get(url,timeout=3)
if response.status_code==200:
  print("Url is working")
else:
  print("Url is not working")