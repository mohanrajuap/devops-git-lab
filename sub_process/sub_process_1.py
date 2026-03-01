from pathlib import Path
path_1=Path("/mnt/c/Users/raju2/OneDrive/Documents/py/happy.txt")
import subprocess
a=subprocess.run(["df","-h"],capture_output=True,text=True)
print(a.stdout)
path_1.write_text("happy")
