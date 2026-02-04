def main():
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    try:
        f1 = open(source, "r")
        f2 = open(destination, "w")

        data = f1.read()
        f2.write(data)

        print("Contents copied successfully")

        f1.close()
        f2.close()

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
