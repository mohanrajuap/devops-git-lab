from pathlib import Path
i=0
Filepath=Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
with Filepath.open('r') as F:
     
  for line_number,line_data in enumerate(F,start=1):
    if "error" in line_data:
      print("ERROR in line",{line_number})
      i += 1
    else:
      print("no errors in file")