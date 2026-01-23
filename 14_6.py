#lambda function which accepts one number and return True if number is odd otherwise false


CheckOdd = lambda No: No%2 == 1


def main():

    num = int(input("Enter a number: "))

    if CheckOdd(num):
        print("True")
    else:
        print ("False") 
    
if __name__=="__main__":
    main()
