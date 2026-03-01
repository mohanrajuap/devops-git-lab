import requests
import json
url="https://httpbin.org/post"
json_1={
  "app": "TCH",
  "status": "OK"
}
response=requests.post(url,json=json_1)
print(response.status_code)
print(response.json())