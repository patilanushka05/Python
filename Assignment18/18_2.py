def Maximum(arr):
    max = arr[0]
    for no in arr:
        if no > max:
            max = no
    return max

def main():
    num = int(input("Enter number of elements: "))
    data =[]
    
    for i in range(num):
        data.append(int(input()))

    result = Maximum(data)
    print("Maximum is: ",result)

if __name__=="__main__":
    main()
