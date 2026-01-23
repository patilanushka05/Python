#lambda function using map() which accepts a list of numbers and 
#returns list of squares of each number

Square = lambda No: No * No

def main():
    Data=[10,20,30,40,50]
    print("Actual data is: ",Data)

    MData=list(map(Square, Data))
    print("Squares : ",MData)

if __name__=="__main__":
    main()