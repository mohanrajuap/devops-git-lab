from pathlib import Path
Path_1=Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
i=0 #couting lines
j=0 #counting error
with Path_1.open('r') as v:
    for linenumb,line_data in enumerate(v,start=1):
        i += 1
        if "ERROR" in line_data:
          j += 1
        if j>5:
         print("ALERT")

            