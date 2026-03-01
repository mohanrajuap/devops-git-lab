import pandas as pd
data_read=pd.read_excel(r"C:\Users\raju2\OneDrive\Documents\py\Book1.xlsx")
print(data_read)
with open("C:/Users/raju2/OneDrive/Documents/py/log.txt",'r')as d:
    vf=d.read()
    print(vf)
