import requests
url = "https://api.github.com/users/octocat"
try:
 response=requests.get(url,timeout=5)
 if response.status_code == 200:
  print("ALL OK")
 else:
  print("URL is not working")
except requests.exceptions.TimeoutError:
    print("time out")