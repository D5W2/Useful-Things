import math
def Poisson(Lambda, y):
    return math.exp(-Lambda) * pow(Lambda, y) / math.factorial(y)
typo_sum = 0
for x in range(11):
    typo_sum += Poisson(25, x)
    print(typo_sum)
print(float(typo_sum))
