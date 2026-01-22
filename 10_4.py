#accepts one number and prints even numbers till that number

def Even(No):
    for i in range(1,No+1):
        if(i % 2 == 0):
            print(i)
def main():
    no = int(input("Enter number: "))
    print("Even numbers are: ")
    Even(no)
    
if __name__=="__main__":
    main()

