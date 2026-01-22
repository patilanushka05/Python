def circle(radius):
    return(3.14*radius*radius)
def main():
    radius= float(input("Enter radius: "))
    

    Area = circle(radius)
    print("Area of Circle is : ",Area)


if __name__=="__main__":
    main()        