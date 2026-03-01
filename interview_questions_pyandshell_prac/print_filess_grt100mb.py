import subprocess
from pathlib import Path

file_path = Path("/mnt/c/Users/raju2/OneDrive/Documents/py")
file_path_1=Path("ENTER YOUT PATH")

result = subprocess.run(
    ["find", ".", "-type", "f", "-size", "+100M"],
    cwd=file_path,
    capture_output=True,
    text=True
)

print(result.stdout)
