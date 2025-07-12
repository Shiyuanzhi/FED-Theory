
# FED模型仿真工具包
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 参数默认值
PARAMS = {
    'μ': 0.1,    # 自主增厚速率
    'λ': 0.3,    # 频度侵蚀系数  
    'σ': 0.2,    # 震荡反馈系数
    'α': 0.5,    # 频度缓冲系数
    'Emax': 1.0  # 壁垒上限
}

def dE_dt(E, t, f, ΔI):
    """信息壁垒动态方程"""
    Γ = ΔI * E / (1 + PARAMS['α']*f)
    return (PARAMS['μ']*E*(1 - E/PARAMS['Emax']) 
            - PARAMS['λ']*f*E 
            + PARAMS['σ']*Γ)

# 模拟运行示例
t = np.linspace(0, 50, 1000)
E0 = 0.5  # 初始壁垒强度
f = 0.8   # 接触频度
ΔI = 0.6  # 信息差异度

E = odeint(dE_dt, E0, t, args=(f, ΔI))

# 可视化
plt.plot(t, E, label=f'f={f}, ΔI={ΔI}')
plt.xlabel('Time (years)'); plt.ylabel('E(t)')
plt.legend(); plt.show()