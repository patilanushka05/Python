#accepts one number and prints count of digits in that number

def CountDigits(no):
    count = 0

    while no != 0:
        count = count + 1
        no = no // 10

    return count


def main():
    num = int(input("Enter a number: "))
    result = CountDigits(num)
    print("Number of digits:", result)


if __name__ == "__main__":
    main()
