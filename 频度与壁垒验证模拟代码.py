import numpy as np
import matplotlib.pyplot as plt

# 参数设置
E0, λ, Emin = 1.0, 0.5, 0.1  # 壁垒参数
α = 0.3                        # 缓冲系数
ΔI = 0.8                       # 固定差异强度

# 计算Γ值
def cognitive_shock(f):
    E = E0 * np.exp(-λ * f) + Emin
    return ΔI * E / (1 + α * f)

# 模拟
f_range = np.linspace(0, 10, 100)
Γ_values = [cognitive_shock(f) for f in f_range]

# 可视化
plt.plot(f_range, Γ_values)
plt.xlabel('Contact Frequency (f)'); plt.ylabel('Cognitive Shock (Γ)')
plt.axvline(x=1/λ - 1/α, color='r', linestyle='--', label='Critical Frequency')
plt.legend(); plt.show()