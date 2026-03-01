from pathlib import Path
flp=Path(input("Please enter the dir to check"))
cnt=0
cnt_error=0
if flp.exists():
   with flp.open("r") as f:
    for linenum, line in enumerate(f,start=1):
       cnt += 1
       if "ERROR" in line:
           cnt_error += 1
print("TOTAL LINES:", cnt)
print("TOTAL ERROR Lines:", cnt_error)             


