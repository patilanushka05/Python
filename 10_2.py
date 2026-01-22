#accepts one number and prints sum of first N natural numbers

def NaturalSum(no):
    total = 0
    for i in range(1, no + 1):
        total = total + i
    print("Sum of natural numbers is:", total)

def main():
    no = int(input("Enter number: "))
    NaturalSum(no)

if __name__ == "__main__":
    main()
