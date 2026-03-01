from datetime import datetime
data1=datetime.now().strftime('%Y%m%d')
filename=f"app_{data1}.log"
print(filename)