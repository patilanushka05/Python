#lambda functions which accepts three number and returns largest number

Maximum=lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)

def main():

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    result = Maximum(num1,num2,num3)
    print(result, "is largest")

if __name__=="__main__":
    main()