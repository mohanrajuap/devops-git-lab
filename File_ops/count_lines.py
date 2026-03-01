from pathlib import Path
file_path = Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
i=0
with file_path.open("r") as G:
    for line_number, line in enumerate(G, start=1):
                  i+= 1 

    print(i)