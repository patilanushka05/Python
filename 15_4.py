#lambda function using reduce() which accepts a list of numbers and 
#returns addition of all elemnts
from functools import reduce

Add = lambda No1,No2 : No1+No2

def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print("Actual data is: ",Data)

    RData=(reduce(Add, Data))
    print("Sum of all elements : ",RData)


if __name__=="__main__":
    main()