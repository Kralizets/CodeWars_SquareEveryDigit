def square_digits(num):
    strTempNum = str(num)
    strResult = ""

    for oneNum in strTempNum:
        strResult += str(int(float(oneNum) * float(oneNum)))
    
    return int(float(strResult))

num1 = 9119
print(square_digits(num1))