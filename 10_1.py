#prg which accepts one  umber and prints multiplication table of that number

def MulTable(no):
    for i in range(1,11):
        print(no*i)
def main():
    no = int(input("Enter number: "))
    MulTable(no)

if __name__=="__main__":
    main()