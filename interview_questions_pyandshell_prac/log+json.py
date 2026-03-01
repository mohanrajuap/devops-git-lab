from pathlib import Path
import json
json_1=Path(r"C:\Users\raju2\OneDrive\Documents\py\json_learn\json_prac.json")
with json_1.open('r') as v:
 a=json.load(v)
x=a.get("error_threshold")
Path_1=Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
Path_2=Path("C:/Users/raju2/OneDrive/Documents/py/log1.txt")
i=0
try:
    with Path_1.open('r') as f:
       for line in f:
          if 'ERROR' in line:
              i +=1
    if i>x:
        with Path_2.open('w') as g:
            u=g.write("Error threshold breached log")
    else:
        with Path_2.open('w') as h:
         m=h.write("system is healty")
except FileNotFoundError:
        print("file not found")
except json.JSONDecodeError:
    print("json error")
finally:
    print("check completed")