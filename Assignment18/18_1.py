def Addition(arr):
    sum=0
    for no in arr:
        sum=sum+no
    return sum

def main():
    num = int(input("Enter number of elements: "))
    data =[]
    
    for i in range(num):
        data.append(int(input()))

    result = Addition(data)
    print("Addition is: ",result)

if __name__=="__main__":
    main()
