#부정적분 해보기
from sympy import *
x = Symbol('x')

f1 = x**3 - 2*x**2 + 3*x + 6

f2 = (4-x**2)**(1/2)

f3 = sin(x) - cos(x)

#정적분 해보기
f1 = x**3 - 2*x**2 + 3*x + 6 #(1 <= x <= 5)

f2 = (4-x**2)**(1/2) #(0 <= x <= 1)

f3 = sin(x) - cos(x) #(0 <= x <= 3)