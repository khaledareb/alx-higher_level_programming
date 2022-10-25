num1, num2 = input("Enter two values to divide: ").split()

try:
    quotient = int(num1) / int(num2)

    print("{}/{}={}".format(num1,num2, quotient))

except ZeroDivisionError:
    print("You cant divide by Zero")
else:
    print("You didnt raise an excpetion")
finally:
    print("I execute no matter what")