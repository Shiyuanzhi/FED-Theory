import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# 参数设置
mu, lambda_, sigma, alpha = 0.12, 0.3, 0.18, 1.0
f_range = np.linspace(0.05, 2.0, 100)
deltaI_range = np.linspace(0.0, 1.0, 100)
F, DI = np.meshgrid(f_range, deltaI_range)

# 计算稳态解
E_star = 1 - (lambda_*F)/mu + (sigma*DI)/(mu*(1 + alpha*F))
E_star = np.clip(E_star, 0, 1)  # 限制在[0,1]区间

# 自定义颜色映射
cmap = LinearSegmentedColormap.from_list("custom", ["#2E86AB", "#F6F5AE", "#F24236"])

# 绘制热力图
plt.figure(figsize=(8, 6))
contour = plt.contourf(F, DI, E_star, levels=20, cmap=cmap, alpha=0.8)
cbar = plt.colorbar(contour)
cbar.set_label('$E^*$ (壁垒稳态强度)', fontsize=12)

# 标记临界频度线
f_crit = mu/lambda_ - 1/alpha
plt.axvline(x=f_crit, color='black', linestyle='--', label=f'临界频度 $f_c={f_crit:.2f}$')

# 标注典型历史案例
plt.scatter([0.08, 1.2], [0.8, 0.6], color='white', s=100, edgecolors='black', 
            label=['明朝海禁', '大英殖民'])
plt.xlabel('接触频度 $f$ (次/年)', fontsize=12)
plt.ylabel('差异化信息强度 $\Delta I$', fontsize=12)
plt.title('壁垒稳态随频度与差异强度的变化', fontsize=14)
plt.legend()
plt.savefig('E_steady_state.png', dpi=300, bbox_inches='tight')
plt.show()