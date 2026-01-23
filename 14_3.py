#lambda functions which accepts two number and return maximum number

Maximum = lambda No1,No2: No1 if No1 > No2 else No2

def main():

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = Maximum(num1,num2)
    print(result, "is maximum")

if __name__=="__main__":
    main()