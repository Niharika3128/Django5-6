
from patching.Demo import Calc

def monkey(self,no1,no2):
    print("I am changing the Code")
    return no1-no2

Calc.add = monkey

c = Calc()
sum = c.add(100,200)
print(sum)

