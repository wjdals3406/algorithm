import sys
from fractions import Fraction

a,b = map(int, sys.stdin.readline().split())
answer = Fraction(a, b)
print(a // answer.numerator)
print((a // answer.numerator) * answer.numerator * answer.denominator)

#유클리드 호제법
