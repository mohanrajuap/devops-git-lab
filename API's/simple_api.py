import requests
url="https://api.github.com/users/octocat"
response=requests.get(url)
if response.status_code == 200:
    print("ALL GOOD")
    data=response.json()
    print(data["login"])
    print(data["id"])
    print(data)