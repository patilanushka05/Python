
def Frequency(arr, frq):
    count=0
    for no in arr:
        if no==frq:
            count=count+1
    return count

def main():
    num = int(input("Enter number of elements: "))
    data=[]

    for i in range(num):
        data.append(int(input()))

    freq=int(input("enter element to search"))

    result =Frequency(data, freq)

    print("frequency is: ", result)


if __name__=="__main__":
    main()

