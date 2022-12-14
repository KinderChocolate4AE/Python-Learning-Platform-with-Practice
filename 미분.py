# 미분 코딩수학 실습 예제
from sympy import * 

# 1. 다항함수 미분해보기
x = Symbol('x')
f1 = 5*x + 2

f2 = 2*x**3 + 4*x**2 + 2*x + 4

# 2. 삼각함수 미분해보기
f3 = 3*cos(2*x + 1) + sin(x)

f4 = cosh(x)

# 3. 유리함수 미분해보기
f5 = (x+3)/(x**2 + 7*x + 9)

f6 = (sin(x) + 3)/(5*x + 3)

# 4. 무리함수 미분해보기
f7 = (x)**(1/2)

f8 = (2*x**2 + 1)**(1/3)