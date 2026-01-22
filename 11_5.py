#accepts one number and checks whether it is pailndrome or not

def Palindrome(no):
    temp = no
    reverse = 0

    while no !=0:
        num = no % 10 
        reverse = reverse * 10 + num
        no = no // 10

    if temp==reverse:
        return True
    else:
        return False


def main():
    num=int(input("Enter number "))
    if Palindrome(num):
        print(num, "is a Palindrome number")
    else:
        print(num, "is Not a Palindrome number")

if __name__=="__main__":
    main()