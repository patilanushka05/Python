#pefect number

def CheckPerfect(no):
    sum = 0

    for i in range(1, no):
        if no % i == 0:
            sum = sum + i

    if sum == no:
        return True
    else:
        return False


def main():
    num = int(input("Enter a number: "))

    if CheckPerfect(num):
        print(num, "is a Perfect number")
    else:
        print(num, "is Not a Perfect number")


if __name__ == "__main__":
    main()