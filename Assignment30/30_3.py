def main():
    filename = input("Enter file name: ")

    try:
        f = open(filename, "r")

        for line in f:
            print(line, end="")

        f.close()

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
