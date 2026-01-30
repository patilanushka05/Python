class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        return False

    def Factors(self):
        print("Factors of", self.Value, ":")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

Obj1 = Numbers(6)

print("Prime:", Obj1.ChkPrime())
print("Perfect:", Obj1.ChkPerfect())
Obj1.Factors()
print("Sum of Factors:", Obj1.SumFactors())
