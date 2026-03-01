import json
from pathlib import Path
config=Path(r"C:\Users\raju2\OneDrive\Documents\py\json_learn\json_prac.json")
with config.open('r') as c:
 v=json.load(c)
if "error_threshold" in v:
    print(v.get("error_threshold"))
else:
    print("Vlaue not exist")