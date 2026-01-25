def CountDigits(No):
    Sum=0
    while No > 0:
        Sum=Sum+(No%10)
        No = No // 10
        Sum += 1
    return Sum


def main():
   n = int(input("Enter number:"))
   result= CountDigits(n)
   print("Length:",result)

if __name__=="__main__":
    main()
