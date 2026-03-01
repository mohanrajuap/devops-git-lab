import requests
import time

url = "https://api.github.com/users/octocat"
retries = 3

try:
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                print("API OK")
                break
            else:
                print("Attempt", attempt, "failed with status", response.status_code)

        except requests.exceptions.Timeout:
            print("Attempt", attempt, "timed out")

        time.sleep(2)

    else:
        # This runs only if loop never breaks
        raise Exception("API Down after retries")

except Exception as e:
    print("ALERT:", e)
