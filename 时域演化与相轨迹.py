from scipy.integrate import odeint

def dE_dt(E, t, f, DeltaI, mu=0.12, lambda_=0.3, sigma=0.18, alpha=1.0):
    Gamma = DeltaI * E / (1 + alpha * f)
    return mu*E*(1-E) - lambda_*f*E + sigma*Gamma

# 时间轴（年）
t = np.linspace(0, 50, 1000)

# 模拟三种场景
cases = [
    {"f": 0.1, "DeltaI": 0.8, "label": "低频高差异（明朝海禁）", "color": "#2E86AB"},
    {"f": 0.5, "DeltaI": 0.4, "label": "中频中差异", "color": "#F6F5AE"},
    {"f": 1.5, "DeltaI": 0.9, "label": "高频高差异（工业革命）", "color": "#F24236"}
]

plt.figure(figsize=(10, 6))
for case in cases:
    E = odeint(dE_dt, E0=0.5, t=t, args=(case["f"], case["DeltaI"]))
    plt.plot(t, E, label=case["label"], color=case["color"], linewidth=2)

plt.xlabel('时间 (年)', fontsize=12)
plt.ylabel('信息壁垒强度 $E(t)$', fontsize=12)
plt.title('不同频度下的壁垒演化轨迹', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('E_evolution.png', dpi=300, bbox_inches='tight')