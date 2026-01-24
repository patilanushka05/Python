def NameLen(n):
    count=0
    for ch in n:
       count=count+1
    return count


def main():
   n = (input("Enter name:"))
   result= NameLen(n)
   print("Length:",result)

if __name__=="__main__":
    main()
