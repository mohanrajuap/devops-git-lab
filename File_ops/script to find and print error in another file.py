from pathlib import Path

# Input log file
source = Path("C:/Users/raju2/OneDrive/Documents/py/system.log")

# Output file 
output = Path("C:/Users/raju2/OneDrive/Documents/py/error_txn.log")

with source.open("r") as f, output.open("w") as out:
    for line in f:
        if "ERROR" in line:
            out.write(line)

print("ERROR lines saved to error_txn.log")
