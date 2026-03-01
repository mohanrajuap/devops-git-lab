from pathlib import Path
K=Path("C:/Users/raju2/OneDrive/Documents/py/backup.log")
if K.exists():
    print("backup.log")
else:
    print("File missing")