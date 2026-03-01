from pathlib import Path
import subprocess

log_file = Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")

result = subprocess.run(["df", "-h"], capture_output=True, text=True)

with open(log_file, "a") as f:
    f.write(result.stdout)
