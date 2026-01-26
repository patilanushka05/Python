from functools import reduce

Check = lambda No: No >= 70 and No <= 90
Increase = lambda No: No + 10
Product = lambda A, B: A * B

def main():
    Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    FData = list(filter(Check, Data))
    MData = list(map(Increase, FData))
    RData = reduce(Product, MData)

    print("List after filter:", FData)
    print("List after map:", MData)
    print("Output of reduce:", RData)

if __name__ == "__main__":
    main()
