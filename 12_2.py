#accept one number and prints its factors

def Factors(no):
    print("Factors are:")
    for i in range(1, no + 1):
        if no % i == 0:
            print(i)


def main():
    num = int(input("Enter a number: "))
    Factors(num)


if __name__ == "__main__":
    main()
