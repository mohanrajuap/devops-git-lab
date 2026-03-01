import logging
import time
import requests

logging.basicConfig(
    filename="C:/Users/raju2/OneDrive/Documents/py/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

url = "https://api.github.com/users/octocat"

try:
    start_time = time.time()
    response = requests.get(url, timeout=5)
    response_time = round(time.time() - start_time, 2)

    if response_time > 2:
        logging.warning(
            f"API is slow | Status={response.status_code} | ResponseTime={response_time}s"
        )
    else:
        logging.info(
            f"API is healthy | Status={response.status_code} | ResponseTime={response_time}s"
        )

except requests.exceptions.Timeout:
    logging.error("API request timed out")
