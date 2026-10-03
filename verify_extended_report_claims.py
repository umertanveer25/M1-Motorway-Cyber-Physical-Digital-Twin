import numpy as np
import scipy.signal as signal
import json

print("=" * 80)
print("EXTENDED VERIFICATION: STRING STABILITY TRANSFER FUNCTION")
print("=" * 80)

# Transfer function H(s) for 22-wheeler trailer:
# H_i(s) = (k_v s^2 + k_p s + k_i) / (tau_b s^4 + s^3 + (k_v + h_i k_p) s^2 + (k_p + h_i k_i) s + k_i)
# Gains: k_p = 0.85, k_v = 1.35, k_i = 0.03
# For 22-wheeler: tau_b = 0.78, mass = 44000 kg, m_ratio = 44000 / 1500 = 29.333
# h_i = 0.6 + 0.5 * 0.78 + 0.03 * sqrt(29.333) = 0.6 + 0.39 + 0.03 * 5.416 = 0.6 + 0.39 + 0.1625 = 1.1525 s (or 1.141 s)
for tau_b, h_i, name in [
    (0.18, 0.72, "Passenger Car"),
    (0.45, 0.92, "Daewoo Bus"),
    (0.78, 1.141, "22-Wheeler (with mass-scaled headway)"),
    (0.78, 0.60, "22-Wheeler (with nominal 0.6s headway)")
]:
    num = [1.35, 0.85, 0.03]  # k_v s^2 + k_p s + k_i
    den = [tau_b, 1.0, 1.35 + 0.85 * h_i, 0.85 + 0.03 * h_i, 0.03] # tau_b s^4 + s^3 + ...
    w = np.linspace(0.01, 10.0, 100000)
    s = 1j * w
    H = (1.35 * s**2 + 0.85 * s + 0.03) / (tau_b * s**4 + s**3 + (1.35 + 0.85 * h_i) * s**2 + (0.85 + 0.03 * h_i) * s + 0.03)
    mag = np.abs(H)
    max_mag = np.max(mag)
    max_w = w[np.argmax(mag)]
    db = 20 * np.log10(max_mag)
    print(f"{name}:")
    print(f"  ||H(jw)||_inf: {max_mag:.4f} ({db:+.2f} dB) at w = {max_w:.2f} rad/s")
    print(f"  String stable? {'YES' if max_mag <= 1.0001 else 'NO (STRICTLY UNSTABLE)'}")

print("\n" + "=" * 80)
print("EXTENDED VERIFICATION: THEIL'S INEQUALITY COEFFICIENT IN BENCHMARK JSON")
print("=" * 80)
with open('results/m1_real_engine_benchmark.json', 'r') as f:
    bench_data = json.load(f)

print("Actual JSON contents:")
for k in ["theil_inequality_coefficient_u", "sim_to_real_fidelity_pct", "ks_test_p_value", "total_energy_kwh_per_100km_dt"]:
    print(f"  {k}: {bench_data.get(k)}")

print("\n" + "=" * 80)
print("EXTENDED VERIFICATION: ADVANCED ML SUITE CODE AUDIT")
print("=" * 80)
with open('controllers/m1_advanced_ml_suite.py', 'r') as f:
    ml_content = f.read()

print(f"Contains 'import torch': {'torch' in ml_content}")
print(f"Contains 'import tensorflow': {'tensorflow' in ml_content}")
print(f"Contains 'import sklearn': {'sklearn' in ml_content}")
print(f"Contains 'import shap': {'shap' in ml_content}")
