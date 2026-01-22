#prg which accepts one number and prints cube of that number

def Cube(No):
    return (No**3)

def main():
    
    a = int(input("Enter Number: "))
    result= Cube(a)
    print("Cube of number is: ",result)
        
if __name__ =="__main__":
    main()