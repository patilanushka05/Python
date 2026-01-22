#prg which accepts one number and checks whether it is prime or not

def Prime(no):
    if no <= 1:
        return False
    
    for i in range(2, int(no/2) + 1):
        if no % i == 0:
            return False
        
    return True


def main():
    num = int(input("Enter a number: "))

    if Prime(num):
        print(num, "is a Prime number")
    else:
        print(num, "is Not a Prime number")


if __name__ == "__main__":
    main()

