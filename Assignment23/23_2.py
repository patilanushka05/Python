class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Deposit(self):
        amt = float(input("Enter deposit amount: "))
        self.Amount = self.Amount + amt

    def Withdraw(self):
        amt = float(input("Enter withdrawal amount: "))
        if amt <= self.Amount:
            self.Amount = self.Amount - amt
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

    def Display(self):
        print("Account Holder:", self.Name)
        print("Balance:", self.Amount)


Obj1 = BankAccount("Anushka", 10000)
Obj1.Deposit()
Obj1.Withdraw()
print("Interest:", Obj1.CalculateInterest())
Obj1.Display()

Obj2 = BankAccount("Yash", 20000)
Obj2.Deposit()
Obj2.Withdraw()
print("Interest:", Obj2.CalculateInterest())
Obj2.Display()

