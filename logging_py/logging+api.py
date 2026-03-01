import logging
import requests
import time
logging.basicConfig(
    filename="C:/Users/raju2/OneDrive/Documents/py/app.logs",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
url="https://api.github.com/users/octocat"
try:
    time_mon=time.time()
    response=requests.get(url,timeout=5)
    time_mon2=round(time.time -time_mon,2)
    if response.status_code==200:
       logging.info(f"response is revivec",{response.status_code})
    else:
        logging.info(f"not a expected response recived",{response.status_code})
except requests.exceptions.Timeout:
    logging.exception("time out happened")