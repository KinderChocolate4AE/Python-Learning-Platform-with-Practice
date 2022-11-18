#부정적분 해보기
from sympy import *
x = Symbol('x')

f1 = x**3 - 2*x**2 + 3*x + 6
print(Derivative(f1, x).doit())

f2 = (4-x**2)**(1/2)
print(Derivative(f2, x).doit())

f3 = sin(x) - cos(x)
print(Derivative(f3, x).doit())

#정적분 해보기
f1 = x**3 - 2*x**2 + 3*x + 6 #(1 <= x <= 5)
print(Integral(f1, (x, 1, 5)).doit())

f2 = (4-x**2)**(1/2) #(0 <= x <= 1)
print(Integral(f2, (x, 0, 1)).doit())

f3 = sin(x) - cos(x) #(0 <= x <= 3)
print(Integral(f3, (x, 0, 3)).doit())