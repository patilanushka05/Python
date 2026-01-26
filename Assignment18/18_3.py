def Minimum(arr):
    min = arr[0]
    for no in arr:
        if no < min:
            min = no
    return min

def main():
    num = int(input("Enter number of elements: "))
    data =[]
    
    for i in range(num):
        data.append(int(input()))

    result = Minimum(data)
    print("Minimum is: ",result)

if __name__=="__main__":
    main()
