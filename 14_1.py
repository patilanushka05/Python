#lambda functions which accepts a number and return square of that number

Square = lambda no : no * no

def main():

    num = int(input("Enter number: "))
    result = Square(num)
    print("Square of number is: ",result)

if __name__=="__main__":
    main()