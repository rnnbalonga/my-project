def isZero(isZero):
    # result = "0" if isZero else "1"
    result = ""
    if isZero:
        result = "0"
    else:
        result = "1"
    print(f"result is {result}")

isZero(False)
isZero(True)