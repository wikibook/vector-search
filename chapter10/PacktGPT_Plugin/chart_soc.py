# 필요한 라이브러리 가져오기
import numpy as np
import matplotlib.pyplot as plt


# 시그모이드를 사용해 SoC 함수 정의하기
def soc_function(R, C, T, A, k=1, threshold=2):
    return 1 / (1 + np.exp(-k * (R + C + T + A - threshold)))


# 샘플 R, C, T, A 값
R_values = np.linspace(0.8, 1, 50)
C_values = np.linspace(0.8, 1, 50)
T_values = np.linspace(0.8, 1, 50)
A_values = np.linspace(0.8, 1, 50)

# 샘플 R, C, T, A 값에 대한 SoC 값 계산.
soc_values = soc_function(R_values, C_values, T_values, A_values)

# 함수 표시
plt.figure(figsize=(10, 6))
plt.plot(R_values, soc_values, label="SoC values", color='blue')
plt.axhline(y=0.5, color='r', linestyle='--', label="Midpoint")
plt.title("Significance of Context (SoC) vs. R (with C, T, A held constant)")
plt.xlabel("Relevance (R)")
plt.ylabel("SoC Value")
plt.legend()
plt.grid(True)
plt.show()
