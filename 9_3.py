#prg which accepts one number and prints square of that number

def Square(No1):
    return (No1**2)

def main():
    
    a = int(input("Enter Number: "))
    result= Square(a)
    print("Square of number is: ",result)
        
if __name__ =="__main__":
    main()