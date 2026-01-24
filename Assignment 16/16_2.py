def ChkNum(No):
    if No%2==0:
        print("Even number")
    else:
        print("Odd number")

def main():
    num = int(input("Enter number: "))
    ChkNum(num)


if __name__=="__main__":
    main()
