def CountDigits(No):
    count=0
    while No != 0:
        No = No // 10
        count += 1
    return count


def main():
   n = int(input("Enter number:"))
   result= CountDigits(n)
   print("Length:",result)

if __name__=="__main__":
    main()
