def rectangle(len,bre):
    return(len*bre)

def main():
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    Area = rectangle(length,breadth)
    print("Area of Rectangle is : ",Area)


if __name__=="__main__":
    main()        