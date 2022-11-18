# 1. 그래프 축을 그리시오
import matplotlib.pyplot as plt

# 2. y=x 그래프를 그리시오
import numpy as np
x=np.linspace(-10, 10, 100)

# 3. 3개의 평균과 표준편차에 따른 정규분포 그래프를 구분하여 한 평면에 그리시오
mu1, sigma1 = map(float, input().split())
mu2, sigma2 = map(float, input().split())
mu3, sigma3 = map(float, input().split())