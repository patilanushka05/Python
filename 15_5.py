#lambda function using reduce() which accepts a list of numbers and 
#returns maximum element
from functools import reduce

Maximum=lambda No1,No2:No1 if No1>No2 else No2

def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print("Actual data is: ",Data)

    RData=(reduce(Maximum, Data))
    print("Maximum elements: ",RData)


if __name__=="__main__":
    main()