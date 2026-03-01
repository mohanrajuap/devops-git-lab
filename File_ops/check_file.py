from pathlib import Path

file_path = Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")

warning_count = 0

with file_path.open() as f:
    for line in enumerate(f, start=1):
        if "WARNING" in line:
            warning_count += 1

            print(line)

print("Total WARNING lines:", warning_count)
