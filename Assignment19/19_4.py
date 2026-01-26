from functools import reduce

Even = lambda No: No % 2 == 0
Square = lambda No: No * No
Add = lambda A, B: A + B

def main():
    Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    FData = list(filter(Even, Data))
    MData = list(map(Square, FData))
    RData = reduce(Add, MData)

    print("List after filter:", FData)
    print("List after map:", MData)
    print("Output of reduce:", RData)

if __name__ == "__main__":
    main()
