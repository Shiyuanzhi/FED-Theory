import numpy as np
import matplotlib.pyplot as plt

# 参数设置
mu = 0.12
lambda_ = 0.3
sigma = 0.18
alpha = 1.0

f_vals = np.linspace(0.05, 2.0, 50)
deltaI_vals = np.linspace(0.0, 1.0, 50)
E_star = np.zeros((len(f_vals), len(deltaI_vals)))

# 解析求解E*（稳态近似）
for i, f in enumerate(f_vals):
    for j, dI in enumerate(deltaI_vals):
        # 解方程: 0 = mu*E*(1-E) - lambda*f*E + sigma*dI*E/(1+alpha*f)
        # ==> mu*(1-E) - lambda*f + sigma*dI/(1+alpha*f) = 0 (E>0)
        numerator = mu - lambda_ * f + sigma * dI / (1 + alpha * f)
        E = numerator / mu
        E_star[i, j] = np.clip(E, 0, 1)  # 限制在[0,1]区间

# 绘制热力图
plt.figure(figsize=(7,5))
plt.imshow(E_star.T, aspect='auto', origin='lower',
           extent=[f_vals[0], f_vals[-1], deltaI_vals[0], deltaI_vals[-1]])
plt.colorbar(label='$E^*$ (壁垒稳态)')
plt.xlabel('接触频度 $f$')
plt.ylabel('差异化信息 $\\Delta I$')
plt.title('壁垒稳态 $E^*$ 随 $f,\\Delta I$ 变化热力图')
plt.tight_layout()
plt.show()
