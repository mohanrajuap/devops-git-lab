import json
from pathlib import Path
config=Path(r"C:\Users\raju2\OneDrive\Documents\py\json_learn\json_prac.json")
with config.open("r") as f:
    data=json.load(f)
    print(data["app name"])
    print(data["app swift limit"])