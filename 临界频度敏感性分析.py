mu_range = np.linspace(0.05, 0.2, 50)
lambda_range = np.linspace(0.1, 0.5, 50)
MU, LAMBDA = np.meshgrid(mu_range, lambda_range)
f_crit = MU / LAMBDA - 1/alpha

plt.figure(figsize=(8, 6))
plt.contourf(MU, LAMBDA, f_crit, levels=20, cmap='viridis')
plt.colorbar(label='临界频度 $f_c$')
plt.xlabel('自主增厚速率 $\mu$', fontsize=12)
plt.ylabel('频度耗散系数 $\lambda$', fontsize=12)
plt.title('临界频度对 $\mu$ 和 $\lambda$ 的敏感性', fontsize=14)
plt.savefig('f_crit_sensitivity.png', dpi=300)