def ChkNum(No):

    if No>0:
        print("Positive number")
    elif No<0:
        print("Negative number")
    else:
        print("Zero")

def main():
    num = int(input("Enter number: "))
    ChkNum(num)


if __name__=="__main__":
    main()
