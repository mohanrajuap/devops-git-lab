from pathlib import Path
file_path = Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
c=open("C:/Users/raju2/OneDrive/Documents/py/log1.txt", "w")

with file_path.open("r") as G:
 for line_numb, line in enumerate(G, start=10):
      if line_numb>20:
          break
      print(line_numb,line)
      c.write(line)
    
  
