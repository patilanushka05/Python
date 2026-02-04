def main():
    filename = input("Enter source file name: ")

    try:
        src = open(filename, "r")
        dest = open("Demo.txt", "w")

        dest.write(src.read())

        print("Contents copied successfully")

        src.close()
        dest.close()

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
