import threading

sum_result = 0
product_result = 1

def Sum(data):
    global sum_result
    sum_result = sum(data)

def Product(data):
    global product_result
    product_result = 1
    for i in data:
        product_result *= i

def main():
    data = list(map(int, input("Enter elements: ").split()))

    t1 = threading.Thread(target=Sum, args=(data,))
    t2 = threading.Thread(target=Product, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum:", sum_result)
    print("Product:", product_result)

if __name__ == "__main__":
    main()
