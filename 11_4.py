#accepts one number and prints reverse

def ReverseNumber(no):
    reverse = 0

    while no !=0:
        num = no % 10 
        reverse = reverse * 10 + num
        no = no // 10

    return reverse

def main():
    num = int(input("Enter number: "))
    result = ReverseNumber(num)
    print("Reverse number: ", result)

if __name__=="__main__":
    main()
        