#lambda function using filter() which accepts a list of numbers and 
#returns the count of even numbers
Even = lambda No: No%2==0

def main():
    Data=[5,15,30,25,90,77,35]
    print("Actual data is: ",Data)

    FData=len(list(filter(Even, Data)))
    print("Count of even numbers: ",FData)

if __name__=="__main__":
    main()    

