import sys

def main():
    if len(sys.argv) != 3:
        print("Invalid arguments")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    try:
        f1 = open(file1, "r")
        f2 = open(file2, "r")

        data1 = f1.read()
        data2 = f2.read()

        if data1 == data2:
            print("Success")
        else:
            print("Failure")

        f1.close()
        f2.close()

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
