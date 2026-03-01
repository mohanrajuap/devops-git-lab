try:
    a = int(input("ENTER VALUE: "))
    if a % 2 == 0:
        print("ALL GOOD")
    else:
        print("ODD NUMBER")
except ValueError:
    print("SEEMS PROVIDED VALUE IS WRONG")
finally:
    print("PRINTING")
