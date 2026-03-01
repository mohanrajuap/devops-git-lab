import json
from pathlib import Path
config=Path(r"C:\Users\raju2\OneDrive\Documents\py\json_learn\json_prac.json")
with config.open("r") as f:
    fz=json.load(f)
    fz["daily check"]=25
    with config.open("w") as f:
     json.dump(fz,f,indent=4)
print(fz)
print(fz["app name"])