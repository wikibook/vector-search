import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 상수
k = 5
threshold = 2

# 시그모이드 함수 정의
def soc_function(R, C, T, A, k, wR=1, wC=1, wT=1, wA=1, threshold=0):
    return 1 / (1 + np.exp(-k * (wR*R + wC*C + wT*T + wA*A - threshold)))

# 1. 시그모이드 함수 곡선
x = np.linspace(-10, 10, 400)
y = 1 / (1 + np.exp(-x))

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title("Figure 1: Sigmoid Function Curve")
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.grid(True)
plt.show()

# 2. 상호작용 3D 그림
from mpl_toolkits.mplot3d import Axes3D

# 예제를 위해 임의의 데이터를 생성했지만, 실제 데이터를 사용하면 더 좋을 수 있습니다.
R_vals = np.linspace(0, 1, 10)
C_vals = np.linspace(0, 1, 10)
T_vals = np.linspace(0, 1, 10)

R, C, T = np.meshgrid(R_vals, C_vals, T_vals)
A_val = 0.5  # 이 예제에서는 단순화를 위해 고정
SoC = soc_function(R, C, T, A_val, k)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(R, C, T, c=SoC.ravel(), cmap='viridis')
ax.set_xlabel('Relevance (R)')
ax.set_ylabel('Continuity (C)')
ax.set_zlabel('Timeliness (T)')
ax.set_title("Figure 2: Interaction of R, C, and T")
fig.colorbar(scatter, ax=ax, label='SoC Value')  # This adds the colorbar
plt.show()

# 3. k의 변화가 미치는 영향
ks = [1, 5, 10]
R_val, C_val, T_val, A_val = 0.5, 0.6, 0.7, 0.8

plt.figure(figsize=(8, 6))


plt.title("Figure 3: Effect of Varying k on SoC")
plt.xlabel("Combined Factors")
plt.ylabel("SoC Value")
plt.legend()
plt.grid(True)
plt.show()

# 4. 가중치의 히트맵
# 단순화를 위해, 두 가중치 간(wR과 wC)의 상호작용을 고려해 보겠습니다.

weights = np.linspace(0, 2, 50)
wR, wC = np.meshgrid(weights, weights)
SoC_heatmap = soc_function(R_val, C_val, T_val, A_val, k, wR, wC)

plt.figure(figsize=(8, 6))
sns.heatmap(SoC_heatmap, cmap='viridis', cbar_kws={'label': 'SoC Value'})
plt.title("Figure 4: Heatmap of Varying wR and wC")
plt.xlabel("Weight of Relevance (wR)")
plt.ylabel("Weight of Continuity (wC)")
plt.xticks(ticks=np.linspace(0, len(weights)-1, 5), labels=np.linspace(0, 2, 5))
plt.yticks(ticks=np.linspace(0, len(weights)-1, 5), labels=np.linspace(0, 2, 5))
plt.show()

# Note : 나머지 그림과 표를 효과적으로 그리기 위해서는 더 구체적인 시나리오나 데이터 세트가 필요합니다.
