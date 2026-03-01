from pathlib import Path
Path_1=Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
with Path_1.open('r') as f:
    i=0
    for line, line_num in enumerate(f, start=1):
       i += 1

    print("total number of lines is", line)