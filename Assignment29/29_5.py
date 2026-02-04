def main():
    filename = input("Enter file name: ")
    word = input("Enter string: ")

    try:
        f = open(filename, "r")
        data = f.read()
        count = data.count(word)
        print("Frequency:", count)
        f.close()

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
