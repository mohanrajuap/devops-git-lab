import requests
import logging
try:
 url="https://api.github.com/users/octocat"
 response=requests.get(url)
