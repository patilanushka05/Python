#check vovel or constant

def Vovel(char):
    char = char.lower()
    if char in ['a','e','i','o','u']:
        return True
    else:
        return False

def main():
    char = input("Enter character: ")
    if Vovel(char):
        print(char, "is a vovel")
    else:
        print(char, "is a constant")


if __name__=="__main__":
    main()