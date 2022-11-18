# 1. 
import matplotlib.pyplot as plt
plt.legend()
plt.show()

# 2.
import numpy as np

x = np.linspace(-10, 10, 100)
#구간 시작점, 구간 끝점, 구간 내 숫자 개수
plt.plot(x, x, color = 'green', label = 'y = x')
#(변수, 그래프, (color='색깔', alpha='투명도(0~1)'), label = 'y=그래프')
#color와 alpha는 안에서 생략 가능
plt.legend()
# 안에서 범례의 위치나 글자 색상 지정
plt.show()

# 3. 
import numpy as np
import matplotlib.pyplot as plt


mu1, sigma1 = map(float, input().split())
mu2, sigma2 = map(float, input().split())
mu3, sigma3 = map(float, input().split())

x = np.linspace(-10, 10, 100)
y1 = (1 / np.sqrt(2 * np.pi * sigma1**2)) * np.exp(-(x-mu1)**2 / (2 * sigma1**2))
y2 = (1 / np.sqrt(2 * np.pi * sigma2**2)) * np.exp(-(x-mu2)**2 / (2 * sigma2**2))
y3 = (1 / np.sqrt(2 * np.pi * sigma3**2)) * np.exp(-(x-mu3)**2 / (2 * sigma3**2))

plt.plot(x, y1, alpha=1)
plt.plot(x, y2, alpha=1)
plt.plot(x, y3, alpha=1)
plt.xlabel('x') #x축에 쓰여지는 값
plt.ylabel('f(x)') #y축에 쓰여지는 값
plt.legend()
plt.show()