#lambda function using filter() which accepts a list of numbers and 
#returns list of odd numbers
Odd = lambda No:No%2==1

def main():
    Data=[1,2,3,4,5,6,7,8]
    print("Actual data is: ",Data)

    FData=list(filter(Odd, Data))
    print("Even list : ",FData)


if __name__=="__main__":
    main()