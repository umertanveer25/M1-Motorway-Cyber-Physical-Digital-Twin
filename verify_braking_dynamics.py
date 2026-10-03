import numpy as np

print("=" * 80)
print("EXTENDED VERIFICATION: EMERGENCY BRAKING & STOPPING DISTANCE DEFICIT")
print("=" * 80)

# Lead Car (V0): a_max = -8.5 m/s^2, tau_l = 0.18 s, reaction/delay = 0.05 s, v0 = 30 m/s
# Road grade: -3.8% down-grade -> theta = -0.038 rad -> a_grade = 9.81 * sin(-0.038) = -0.3727 m/s^2
# Net braking deceleration: a_net = a_max - a_grade = -8.5 - (-0.3727) = -8.1273 m/s^2
# d_stop = v0 * (t_react + tau) + v0^2 / (2 * |a_net|)

v0 = 30.0
grade_acc = 9.81 * 0.038 # 0.37278 m/s^2 downhill acceleration (reducing net braking decel)

# V0 Lead Car:
a_max_0 = 8.5
a_net_0 = a_max_0 - grade_acc # 8.1272 m/s^2
t_lag_0 = 0.05 + 0.18
d_stop_0 = v0 * t_lag_0 + (v0**2) / (2.0 * a_net_0)

# V1 Daewoo Bus:
a_max_1 = 5.2
a_net_1 = a_max_1 - grade_acc # 4.8272 m/s^2
t_lag_1 = 0.20 + 0.45
d_stop_1 = v0 * t_lag_1 + (v0**2) / (2.0 * a_net_1)

# V2 22-Wheeler Trailer:
a_max_2 = 3.6
a_net_2 = a_max_2 - grade_acc # 3.2272 m/s^2
t_lag_2 = 0.38 + 0.78
d_stop_2 = v0 * t_lag_2 + (v0**2) / (2.0 * a_net_2)

print(f"Lead Car V0 Stopping Distance:       {d_stop_0:.2f} m (Report: 62.25 m)")
print(f"Daewoo Bus V1 Stopping Distance:     {d_stop_1:.2f} m (Report: 112.67 m)")
print(f"22-Wheeler V2 Stopping Distance:     {d_stop_2:.2f} m (Report: 174.12 m)")

deficit_1 = d_stop_1 - d_stop_0
deficit_2 = d_stop_2 - d_stop_0

# Target headways:
# Bus behind Lead Car: d_target = d_standstill (14.0) + h_1 (0.920) * 30 = 14.0 + 27.61 = 41.61 m
h_bus = 0.6 + 0.5 * 0.45 + 0.03 * np.sqrt(15000.0 / 1500.0) # 0.6 + 0.225 + 0.09487 = 0.91987 s
gap_bus = 14.0 + h_bus * v0
penetration_bus = gap_bus - deficit_1

# Trailer behind Lead Car:
h_trailer = 0.6 + 0.5 * 0.78 + 0.03 * np.sqrt(44000.0 / 1500.0) # 1.1525 s
gap_trailer = 18.0 + h_trailer * v0
penetration_trailer = gap_trailer - deficit_2

print(f"\nBus vs Car Deficit: {deficit_1:.2f} m | Headway provided: {gap_bus:.2f} m | Net Margin: {penetration_bus:.2f} m (<0 -> CRASH)")
print(f"Trailer vs Car Deficit: {deficit_2:.2f} m | Headway provided: {gap_trailer:.2f} m | Net Margin: {penetration_trailer:.2f} m (<0 -> CRASH)")
