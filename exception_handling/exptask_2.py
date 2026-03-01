filepath=open("C:/Users/raju2/OneDrive/Documents/py/log.txt","r")
G=filepath.read()
try:
      if "ERROR" in G:
        print("FOUND ERROR in LOG")
except:
    print("SEEMS NO ERROR")
finally:
    print("Daily check completed")
    