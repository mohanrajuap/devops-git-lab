try:
    a=int(input("ENTER A VALUE"))
    if a % 2== 0:
        print("A is an even number")
    elif a % 2!= 0:
        print("A is a odd number")
except:
    print("A is not a correct input")
finally:
    print("check completed")