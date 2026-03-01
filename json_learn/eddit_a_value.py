import json
from pathlib import Path
config = Path(r"C:\Users\raju2\OneDrive\Documents\py\json_learn\json_prac.json")
with config.open("r") as f:
    data = json.load(f)
data["daily check"] = 30
with config.open("w") as f:
    json.dump(data, f, indent=4)
print("daily check updated safely")
