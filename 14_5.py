#lambda function which accepts one number and return True if number is even otherwise false


CheckEven = lambda No: No%2 == 0


def main():

    num = int(input("Enter a number: "))

    if CheckEven(num):
        print("True")
    else:
        print ("False") 
    
if __name__=="__main__":
    main()
