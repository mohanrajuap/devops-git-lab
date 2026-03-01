from pathlib import Path
import subprocess
out_file = Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
result = subprocess.run(["df", "-h"], capture_output=True, text=True)
if "80" in result:
   out_file.write_text("HAVING HIGH CPU USGAE")
else:
 out_file.write_text("SYSTEM is normal")