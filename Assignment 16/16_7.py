def Divisiblity(No):

    if No%5==0:
        return True
    else:
        return False
    
def main():
    num = int(input("Enter Number: "))
    result= Divisiblity(num)
    print(result)
    


if __name__=="__main__":
    main()
