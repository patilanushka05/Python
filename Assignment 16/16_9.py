def displayEven(n):
    count=0
    no=1
    while count<n:
        if no%2==0:
            print(no)
            count=count+1
        no=no+1


def main():
   n= int(input("Enter n:"))

   displayEven(n)
if __name__=="__main__":
    main()
