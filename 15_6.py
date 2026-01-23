#lambda function using reduce() which accepts a list of numbers and 
#returns minimum element
from functools import reduce

Minimum=lambda No1,No2:No1 if No1<No2 else No2

def main():
    Data=[14,23,56,72,21,11,94,75]
    print("Actual data is: ",Data)

    RData=(reduce(Minimum, Data))
    print("Minimum element: ",RData)


if __name__=="__main__":
    main()