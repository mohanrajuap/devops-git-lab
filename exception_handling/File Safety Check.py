from pathlib import Path
filepath=Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
try:
    if filepath.exists():
        print("FILE FOUND IN PATH")
except  FileNotFoundError:
    print("SEEMS FILE NOT FOUND")

finally:
    print("DAILY CHECK COMPLETED")