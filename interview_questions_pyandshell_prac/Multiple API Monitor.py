import requests
url = ["https://api.github.com/users/octocat","https://api.github.com/users/octocat"]
for line in url:
    response=requests.get(line)
    if response.status_code==200:
        print("the url is working",line)
    else:
        print("the url is not working",line)
    