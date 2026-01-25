def display(No):
    for i in range(1,No+1):
        for j in range(No):
            print(i,end="")
        print()

  
def main():
    No = int(input("Enter number: "))
    (display(No))


if __name__=="__main__":
    main()    