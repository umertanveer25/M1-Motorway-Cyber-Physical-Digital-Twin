import numpy as np
import scipy.stats as stats
import math

print("=" * 80)
print("TASK 1: CHI-SQUARE DEGREES OF FREEDOM & NOISE COVARIANCE AUDIT")
print("=" * 80)

# 1. Degrees of Freedom critical values
df2_crit_01 = stats.chi2.ppf(0.99, df=2)
df3_crit_01 = stats.chi2.ppf(0.99, df=3)
df3_crit_05 = stats.chi2.ppf(0.95, df=3)
actual_pval_921_df3 = 1.0 - stats.chi2.cdf(9.21034037, df=3)
actual_pval_9210_df3 = 1.0 - stats.chi2.cdf(9.21, df=3)

print(f"chi^2_0.01(2) critical value: {df2_crit_01:.6f}")
print(f"chi^2_0.01(3) critical value: {df3_crit_01:.6f}")
print(f"chi^2_0.05(3) critical value: {df3_crit_05:.6f}")
print(f"Tail probability P(chi^2(3) > 9.21034): {actual_pval_921_df3:.6f} (FAR = {actual_pval_921_df3*100:.2f}%)")
print(f"Tail probability P(chi^2(3) > 9.21):    {actual_pval_9210_df3:.6f} (FAR = {actual_pval_9210_df3*100:.2f}%)")

# 2. Covariance of correlated residuals
# Residuals share v2x noise:
# r1 = nu_v2x - nu_radar
# r2 = nu_v2x - nu_optical
# r3 = nu_v2x - nu_byzantine
N_sim = 1_000_000
sigma_v2x = 0.10
sigma_radar = 0.12
sigma_optical = 0.25
sigma_byz = 0.16

nu_v2x = np.random.normal(0, sigma_v2x, N_sim)
nu_radar = np.random.normal(0, sigma_radar, N_sim)
nu_optical = np.random.normal(0, sigma_optical, N_sim)
nu_byz = np.random.normal(0, sigma_byz, N_sim)

r1 = nu_v2x - nu_radar
r2 = nu_v2x - nu_optical
r3 = nu_v2x - nu_byz

R_mat = np.column_stack([r1, r2, r3])
emp_cov = np.cov(R_mat, rowvar=False)

print("\nTheoretical Covariance Matrix:")
theo_cov = np.array([
    [sigma_v2x**2 + sigma_radar**2, sigma_v2x**2, sigma_v2x**2],
    [sigma_v2x**2, sigma_v2x**2 + sigma_optical**2, sigma_v2x**2],
    [sigma_v2x**2, sigma_v2x**2, sigma_v2x**2 + sigma_byz**2]
])
print(theo_cov)
print("\nEmpirical Sample Covariance Matrix (1,000,000 trials):")
print(emp_cov)

# Test unwhitened sum vs Mahalanobis distance
unwhitened_stat = (r1 / np.sqrt(sigma_v2x**2 + sigma_radar**2))**2 + \
                  (r2 / np.sqrt(sigma_v2x**2 + sigma_optical**2))**2 + \
                  (r3 / np.sqrt(sigma_v2x**2 + sigma_byz**2))**2

cov_inv = np.linalg.inv(theo_cov)
mahalanobis_stat = np.sum((R_mat @ cov_inv) * R_mat, axis=1)

print(f"\nUnwhitened stat mean: {np.mean(unwhitened_stat):.4f} (expected 3.0), var: {np.var(unwhitened_stat):.4f} (chi^2(3) var = 6.0)")
print(f"Mahalanobis stat mean: {np.mean(mahalanobis_stat):.4f} (expected 3.0), var: {np.var(mahalanobis_stat):.4f} (chi^2(3) var = 6.0)")
print(f"P(unwhitened > 9.21): {np.mean(unwhitened_stat > 9.21):.6f}")
print(f"P(mahalanobis > 9.21): {np.mean(mahalanobis_stat > 9.21):.6f}")


print("\n" + "=" * 80)
print("TASK 2: GRADUAL DRIFT EVASION AUDIT")
print("=" * 80)

# delta s(t) = 0.5 * 0.05 * t^2 = 0.025 * t^2
# In Swabi fog: fog_density = 0.85, rain_rate = 0
fog_density = 0.85
thresh_adaptive = 9.21 * (1.0 + 0.35 * fog_density)
print(f"Adaptive threshold in Swabi fog: {thresh_adaptive:.6f} (~11.95)")

# Scenario 1: Dual-spoofing drift or radar tracks drift, outside RSU gantry
# chi_sq = (r_optical / 0.25)^2 = (delta_s / 0.25)^2 = 16 * delta_s^2
delta_s_crit_opt = np.sqrt(thresh_adaptive / 16.0)
t_evade_opt = np.sqrt(delta_s_crit_opt / 0.025)
steps_50hz_opt = t_evade_opt * 50.0

print(f"Scenario 1 (Optical only, 1/0.25^2 = 16):")
print(f"  Critical drift delta_s: {delta_s_crit_opt:.6f} m")
print(f"  Evasion time: {t_evade_opt:.6f} s (~5.88 s)")
print(f"  Control steps at 50 Hz: {steps_50hz_opt:.2f} steps (~294-300 steps)")

# Scenario 2: What about all three terms active?
# R_k_adaptive at fog = 0.85:
R_k_adaptive = 0.12 * (1.0 + 1.8 * fog_density)
coef_all = (1.0 / (R_k_adaptive**2)) + (1.0 / 0.25**2) + (1.0 / 0.16**2)
delta_s_crit_all = np.sqrt(thresh_adaptive / coef_all)
t_evade_all = np.sqrt(delta_s_crit_all / 0.025)
steps_50hz_all = t_evade_all * 50.0
print(f"Scenario 2 (All 3 terms active: coef = {coef_all:.4f}):")
print(f"  Critical drift delta_s: {delta_s_crit_all:.6f} m")
print(f"  Evasion time: {t_evade_all:.6f} s")
print(f"  Control steps at 50 Hz: {steps_50hz_all:.2f} steps")

# Scenario 3: Inter-RSU gap with V2X-only drift (Optical + Radar active):
coef_opt_radar = (1.0 / (R_k_adaptive**2)) + (1.0 / 0.25**2)
delta_s_crit_opt_radar = np.sqrt(thresh_adaptive / coef_opt_radar)
t_evade_opt_radar = np.sqrt(delta_s_crit_opt_radar / 0.025)
steps_50hz_opt_radar = t_evade_opt_radar * 50.0
print(f"Scenario 3 (Inter-RSU gap, Radar + Optical active: coef = {coef_opt_radar:.4f}):")
print(f"  Critical drift delta_s: {delta_s_crit_opt_radar:.6f} m")
print(f"  Evasion time: {t_evade_opt_radar:.6f} s")
print(f"  Control steps at 50 Hz: {steps_50hz_opt_radar:.2f} steps")


print("\n" + "=" * 80)
print("TASK 3: MORAN'S I STATISTICAL SIGNIFICANCE AUDIT")
print("=" * 80)

z_moran = 0.6875
phi_z = stats.norm.cdf(z_moran)
one_minus_phi = 1.0 - phi_z
p_val_two_tailed = 2.0 * (1.0 - stats.norm.cdf(abs(z_moran)))

print(f"Given Moran's I z-score: z = {z_moran}")
print(f"Standard Normal CDF Phi(0.6875): {phi_z:.6f}")
print(f"Upper tail 1 - Phi(0.6875):      {one_minus_phi:.6f}")
print(f"True two-tailed p-value:         {p_val_two_tailed:.6f} (~0.4918)")
print(f"Code claim:                       < 1e-4")
print(f"Discrepancy factor:              True p is {p_val_two_tailed / 1e-4:.1f}x higher than 1e-4")
print(f"Is p < 0.05?                     {p_val_two_tailed < 0.05} (FAILS significance, consistent with spatial randomness)")


print("\n" + "=" * 80)
print("TASK 4: ODDS RATIO CONFIDENCE INTERVAL AUDIT")
print("=" * 80)

a = 14759
b = 38931495
c = 0.5
d = 38946254

or_point = (a * d) / (b * c)
print(f"Contingency Table: a={a}, b={b}, c={c}, d={d}")
print(f"Odds Ratio point estimate: {or_point:.6f} (~29529.2)")

# Woolf's method:
ln_or = np.log(or_point)
var_ln_or = (1.0 / a) + (1.0 / b) + (1.0 / c) + (1.0 / d)
se_ln_or = np.sqrt(var_ln_or)

print(f"ln(OR): {ln_or:.6f}")
print(f"Var(ln OR): {var_ln_or:.8f}")
print(f"SE(ln OR): {se_ln_or:.6f}")

# Check with z = 1.959963984540054 (exact 95%) and z = 1.96
for z_val, name in [(stats.norm.ppf(0.975), "Exact z_0.975 (1.95996)"), (1.96, "Standard z=1.96")]:
    ci_lower = np.exp(ln_or - z_val * se_ln_or)
    ci_upper = np.exp(ln_or + z_val * se_ln_or)
    print(f"\n{name}:")
    print(f"  95% CI: [{ci_lower:.1f}, {ci_upper:.1f}]")

# What if Haldane-Anscombe (+0.5 on all 4 cells)?
a_h, b_h, c_h, d_h = a + 0.5, b + 0.5, 0.5, d + 0.5
or_h = (a_h * d_h) / (b_h * c_h)
ln_or_h = np.log(or_h)
se_h = np.sqrt(1.0/a_h + 1.0/b_h + 1.0/c_h + 1.0/d_h)
ci_lower_h = np.exp(ln_or_h - 1.96 * se_h)
ci_upper_h = np.exp(ln_or_h + 1.96 * se_h)
print(f"\nHaldane-Anscombe (+0.5 on all cells, z=1.96):")
print(f"  OR: {or_h:.1f}, 95% CI: [{ci_lower_h:.1f}, {ci_upper_h:.1f}]")

# Let's check how [1846.3, 472147.2] was obtained:
# Let's solve for z or SE or rounding that gives exactly 1846.3 and 472147.2:
for z_test in np.linspace(1.959, 1.961, 201):
    low = np.exp(ln_or - z_test * se_ln_or)
    high = np.exp(ln_or + z_test * se_ln_or)
    if abs(low - 1846.3) < 0.1 or abs(high - 472147.2) < 1.0:
        print(f"Found match: z={z_test:.6f} -> [{low:.1f}, {high:.1f}]")

# What if SE was approximated as sqrt(1/c) = sqrt(2) = 1.41421356?
se_approx = np.sqrt(2.0)
for z_test in [1.96, stats.norm.ppf(0.975)]:
    low = np.exp(ln_or - z_test * se_approx)
    high = np.exp(ln_or + z_test * se_approx)
    print(f"With SE=sqrt(2), z={z_test:.5f} -> [{low:.1f}, {high:.1f}]")

# What if log was rounded?
print(f"Check log rounding: ln(29529.2) - 1.96*1.4142 = {np.log(29529.2) - 1.96*1.4142:.6f}")
print(f"exp: {np.exp(np.log(29529.2) - 1.96*1.4142):.1f}, exp: {np.exp(np.log(29529.2) + 1.96*1.4142):.1f}")
