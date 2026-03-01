from pathlib import Path
Path_1=Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
with Path_1.open('r') as f:
    data=f.read()
    print(data)