import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def dE_dt(E, t, f, μ=0.1, Emax=1, λ=0.3, σ=0.2):
    Γ = 0.8 * E / (1 + 0.5*f)  # Γ(f,E)简化版
    return μ*E*(1-E/Emax) - λ*f*E + σ*Γ

t = np.linspace(0, 50, 1000)
E0 = 0.5  # 初始壁垒

# 模拟不同频度下的E(t)
for f in [0.1, 0.5, 2.0]:
    E = odeint(dE_dt, E0, t, args=(f,))
    plt.plot(t, E, label=f'f={f}')

plt.xlabel('Time'); plt.ylabel('E(t)'); plt.legend()
plt.show()