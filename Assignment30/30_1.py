def main():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")
        count = 0

        for line in file:
            count = count+ 1

        print("Total number of lines:", count)
        file.close()

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
