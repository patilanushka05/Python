#prg which accepts one number and checks whether divisible by 3 and 5 both 

def divisiblity(No):
    if(No%3==0 and No%5==0):
        print("Number is divisible by both 3 and 5 ")
    else:
        print("Number is not divisible by both 3 and 5 ")

def main():
    
    a = int(input("Enter Number: "))
    divisiblity(a)
    
        
if __name__ =="__main__":
    main()