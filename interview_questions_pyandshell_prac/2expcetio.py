from pathlib import Path
Path_1=Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
try:
    if Path_1.exists():
     with Path_1.open('r') as f:
             print("file is exists",f)

except FileNotFoundError:
    print("File not found in path")

except PermissionError:
    print("files but uable to read")
   