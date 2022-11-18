from sympy import *
# 1.
x = Symbol('x')
f1 = 5*x + 2
print(Derivative(f1, x).doit())

f2 = 2*x**3 + 4*x**2 + 2*x + 4
print(Derivative(f2, x).doit())

# 2.
f3 = 3*cos(2*x + 1) + sin(x)
print(Derivative(f3, x).doit())

f4 = cosh(x)
print(Derivative(f4, x).doit())

# 3.
f5 = (x+3)/(x**2 + 7*x + 9)
print(Derivative(f5, x).doit())

f6 = (sin(x) + 3)/(5*x + 3)
print(Derivative(f6, x).doit())

# 4.
f7 = (x)**(1/2)
print(Derivative(f7, x).doit())

f8 = (2*x**2 + 1)**(1/3)
print(Derivative(f8, x).doit())