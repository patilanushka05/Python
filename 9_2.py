#Function ChkGreater that accepts two number and prints Greater number

def ChkGreater(No1,No2):
    if(No1 > No2):
        print(No1,"is greater ")
    elif(No2>No1):
        print(No2, "is greater")
    else:
        print("Both are equal ") 

def main():
    
    a = int(input("Enter first Number: "))
    b = int(input("Enter second Number: "))

    ChkGreater(a,b)
    
if __name__ =="__main__":
    main()
