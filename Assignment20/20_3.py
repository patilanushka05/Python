import threading

def EvenList(data):
    even_list = []
    total = 0
    for i in data:
        if i % 2 == 0:
            even_list.append(i)
            total += i
    print("Even elements:", even_list)
    print("Sum of even elements:", total)

def OddList(data):
    odd_list = []
    total = 0
    for i in data:
        if i % 2 != 0:
            odd_list.append(i)
            total += i
    print("Odd elements:", odd_list)
    print("Sum of odd elements:", total)

def main():
    data = []
    n = int(input("Enter number of elements: "))
    
    for i in range(n):
        value = int(input("Enter element: "))
        data.append(value)

    t1 = threading.Thread(target=EvenList, args=(data,))
    t2 = threading.Thread(target=OddList, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
