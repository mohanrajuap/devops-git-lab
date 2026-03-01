from pathlib import Path
Path_1=Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
with Path_1.open('r') as F:
 error_count=0
 try:
  for line in F:
        if "ERROR" in line:
         error_count += 1
  if error_count > 12:
   raise Exception("Error count is increased")
 except Exception as E:
  print("Alert",E)