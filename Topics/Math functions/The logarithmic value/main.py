from math import log

operand, base = int(input()), int(input())
if base <= 1:
    print(round(log(operand), 2))
else:
    print(round(log(operand, base), 2))
