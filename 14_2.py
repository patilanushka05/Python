#lambda functions which accepts a number and return cube of that number

Cube = lambda no : no **3

def main():

    num = int(input("Enter number: "))
    result = Cube(num)
    print("Cube of number is: ",result)

if __name__=="__main__":
    main()