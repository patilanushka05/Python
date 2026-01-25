import Airthmetic

def main():
    
    No1=int(input("Enter First number: "))
    No2=int(input("Enter Second number: "))


    AddResult = Airthmetic.Add(No1, No2)
    SubResult = Airthmetic.Sub(No1, No2)
    MulResult = Airthmetic.Mul(No1, No2)
    DivResult = Airthmetic.Div(No1, No2)

    print("Addition is:", AddResult)
    print("Subtraction is:", SubResult)
    print("Multiplication is:", MulResult)
    print("Division is:", DivResult)

if __name__ == "__main__":
    main()