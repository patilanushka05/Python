def main():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")
        data = file.read()
        words = data.split()
        print("Total number of words:", len(words))
        file.close()

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
