print("1️ FileNotFoundError")
try:
    open("no_such_file.txt")
except FileNotFoundError as e:
    print(e)

print("\n PermissionError")
try:
    open("/root/secret.txt")
except PermissionError as e:
    print(e)

print("\n ValueError")
try:
    int("abc")
except ValueError as e:
    print(e)

print("\n TypeError")
try:
    "10" + 5
except TypeError as e:
    print(e)

print("\n ZeroDivisionError")
try:
    10 / 0
except ZeroDivisionError as e:
    print(e)

print("\n IndexError")
try:
    a = [1, 2]
    print(a[5])
except IndexError as e:
    print(e)

print("\n KeyError")
try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print(e)

print("\n AttributeError")
try:
    "hello".append("x")
except AttributeError as e:
    print(e)

print("\n NameError")
try:
    print(x)
except NameError as e:
    print(e)

print("\n ModuleNotFoundError")
try:
    import fake_module
except ModuleNotFoundError as e:
    print(e)

print("\n✅ Script completed")
