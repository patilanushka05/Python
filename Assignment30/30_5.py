def main():
    filename = input("Enter file name: ")
    word = input("Enter word to search: ")

    try:
        f = open(filename, "r")
        data = f.read()

        if word in data:
            print("Word found")
        else:
            print("Word not found")

        f.close()

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
