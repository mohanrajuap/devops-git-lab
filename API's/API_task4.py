import requests
import time

url = "https://api.github.com/users/octocat"

for attempt in range(1, 4):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            print("Login:", data.get("login", "N/A"))
            print("Public repos:", data.get("public_repos", "N/A"))
            break
        else:
            print(f"Attempt {attempt}: Status code {response.status_code}")

    except requests.exceptions.Timeout:
        print(f"Attempt {attempt}: Timeout occurred")

    time.sleep(2)

else:
    print("API FAILED after 3 retries")


####