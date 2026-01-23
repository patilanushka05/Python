#lambda function using filter() which accepts a list of strings and 
#returns list of strinh having greater that 5


Length=lambda s:len(s) > 5

def main():
    Data = ["Name","program","city","Marvellous"]
    print("Actual data is: ",Data)

    FData=list(filter(Length, Data))
    print("Strings with length > 5: ",FData)

 
if __name__=="__main__":
    main()
