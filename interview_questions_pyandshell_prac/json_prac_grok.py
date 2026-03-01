import json
from pathlib import Path
json_1=Path(r"C:\Users\raju2\OneDrive\Documents\py\json_learn\json_prac.json")
if json_1.exists():
 with json_1.open('r') as V:
    d=json.load(V)
    c=d.get("database")
    print(c)