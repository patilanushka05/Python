import MarvellousNum

def ListPrime(arr):
    sum = 0
    for no in arr:
        if MarvellousNum.ChkPrime(no):
            sum = sum + no
    return sum

def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input()))

    result = ListPrime(data)
    print("Addition of prime numbers is:", result)

if __name__ == "__main__":
    main()