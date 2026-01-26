import threading

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def Prime(data):
    print("Prime numbers:")
    for i in data:
        if isPrime(i):
            print(i, end=" ")
    print()

def NonPrime(data):
    print("Non-prime numbers:")
    for i in data:
        if not isPrime(i):
            print(i, end=" ")
    print()

def main():
    data = [10, 11, 12, 13, 14, 15]

    t1 = threading.Thread(target=Prime, args=(data,))
    t2 = threading.Thread(target=NonPrime, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
