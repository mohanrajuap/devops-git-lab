from pathlib import Path
Path_1=Path("C:/Users/raju2/OneDrive/Documents/py/status.log")
with Path_1.open('r') as F:
    if "ERROR" in F:
        print("error found in log")
    else:
        print("error not found in log")