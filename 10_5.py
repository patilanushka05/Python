#accepts one number and prints odd numbers till that number

def Odd(No):
    for i in range(1,No+1):
        if(i % 2 == 1):
            print(i)
def main():
    no = int(input("Enter number: "))
    print("Odd numbers are: ")
    Odd(no)
    
if __name__=="__main__":
    main()

