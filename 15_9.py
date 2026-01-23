#lambda function using reduce() which accepts a list of numbers and 
#returns product of all number
from functools import reduce

Product=lambda No1,No2:No1*No2

def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print("Actual data is: ",Data)

    RData=(reduce(Product, Data))
    print("Product of all elements: ",RData)


if __name__=="__main__":
    main()