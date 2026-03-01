import json
from pathlib import Path
config=Path(r"C:\Users\raju2\OneDrive\Documents\py\json_learn\json_prac.json")
with config.open("r") as f:
    data=json.load(f)
if data["app swift limit"] >5:
    print("swift value is exceed the limt")
else:
    print("swift value is in inner limit")