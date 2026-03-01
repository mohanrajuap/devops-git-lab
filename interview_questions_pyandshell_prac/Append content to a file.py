from pathlib import Path
Path_1=Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
with Path_1.open('a') as f:
    c=f.write("INFO Script executed successfully")