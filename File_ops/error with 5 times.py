from pathlib import Path

file_path = Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")


i = 0

with file_path.open("r") as G:
    for line_num, line in enumerate(G, start=1):
        if "ERROR" in line:
            i += 1              
            print(line_num, line)
            if i == 5:          
                break

      