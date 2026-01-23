#lambda function which accepts one number and returns True if divisible by 5

Divisiblity = lambda No: No %5==0

def main():

    num = int(input("Enter a number: "))

    if Divisiblity(num):
        print("True")
    else:
        print ("False") 
    
if __name__=="__main__":
    main()