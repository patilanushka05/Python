from functools import reduce

Prime = lambda No: No > 1 and all(No % i != 0 for i in range(2, No))
Double = lambda No: No * 2
Max = lambda A, B: A if A > B else B

def main():
    Data = [2, 70, 11, 10, 17, 23, 31, 77]

    FData = list(filter(Prime, Data))
    MData = list(map(Double, FData))
    RData = reduce(Max, MData)

    print("List after filter:", FData)
    print("List after map:", MData)
    print("Output of reduce:", RData)

if __name__ == "__main__":
    main()
