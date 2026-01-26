import threading

def Maximum(data):
    print("Maximum element:", max(data))

def Minimum(data):
    print("Minimum element:", min(data))

def main():
    data = list(map(int, input("Enter elements: ").split()))

    t1 = threading.Thread(target=Maximum, args=(data,))
    t2 = threading.Thread(target=Minimum, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
