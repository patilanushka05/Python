def Numbers(no):
    for i in range (no, 0, -1):
        print(i)

def main():
    num = int(input("Enter a number: "))
    Numbers(num)

if __name__=="__main__":
    main()
    