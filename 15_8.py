#lambda function using filter() which accepts a list of strings and 
#returns list of numbers divisible by both 3 and 5
Divisiblity = lambda No: No%3==0 and No%5==0

def main():
    Data=[5,15,30,25,90,77,35]
    print("Actual data is: ",Data)

    FData=list(filter(Divisiblity, Data))
    print("Numbers divisible by both 3 and 5: ",FData)

if __name__=="__main__":
    main()    

