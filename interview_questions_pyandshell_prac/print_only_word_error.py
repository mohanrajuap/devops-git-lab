from pathlib import Path
import subprocess

Path_1 = Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")

error_lines = []   # collect all errors

with Path_1.open('r') as f:
    for line_num, line_data in enumerate(f, start=1):
        if "ERROR" in line_data:
            print(line_data)
            error_lines.append(line_data)

if error_lines:
    error_text = "".join(error_lines)

    subprocess.run(
        f'echo "{error_text}" | mail -s "ERROR found in log" aad@gmail.com',
        shell=True
    )
