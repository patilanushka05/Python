#accepts one number and prints sum of digits

def SumOfDigits(no):
    sum = 0

    while no != 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    return sum


def main():
    num = int(input("Enter a number: "))
    result = SumOfDigits(num)
    print("Sum of digits:", result)


if __name__ == "__main__":
    main()

