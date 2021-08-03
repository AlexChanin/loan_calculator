# put your python code here
from math import sqrt

a, b, c = int(input()), int(input()), int(input())
p = (a + b + c) / 2
square = sqrt(p * (p - a) * (p - b) * (p - c))
print(square)
