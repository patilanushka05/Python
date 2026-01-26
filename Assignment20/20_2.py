import threading

def EvenFactor(No):
    sum_even = 0
    print("Even factors:")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            print(i)
            sum_even += i
    print("Sum of even factors:", sum_even)

def OddFactor(No):
    sum_odd = 0
    print("Odd factors:")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            print(i)
            sum_odd += i
    print("Sum of odd factors:", sum_odd)

def main():
    No = int(input("Enter number: "))

    t1 = threading.Thread(target=EvenFactor, args=(No,))
    t2 = threading.Thread(target=OddFactor, args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
