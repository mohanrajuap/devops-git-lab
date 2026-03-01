from pathlib import Path
Path_1=Path("C:/Users/raju2/OneDrive/Documents/py/log.txt")
with Path_1.open('r') as f:
    error_count=0
    for line_num,line_data in enumerate(f,start=1):
     if "ERROR" in line_data:
        error_count += 1
    print("total count is:",error_count)