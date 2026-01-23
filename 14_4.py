#lambda function which accepts two numbers and returns minimum number

Minimum = lambda No1,No2: No1 if No1 < No2 else No2

def main():

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = Minimum(num1,num2)
    print(result, "is minimum")

if __name__=="__main__":
    main()