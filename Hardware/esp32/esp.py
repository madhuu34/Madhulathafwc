import math

# Define constants for the circuit using values from Q54
L_VALUE_H = 1.0e-3      # Inductance L = 1 mH = 1 * 10^-3 Henry
C_VALUE_F = 10.0e-6     # Capacitance C = 10 uF = 10 * 10^-6 Farad
VS_VALUE_V = 100.0      # Source Voltage Vs = 100 Volts (from Q55)
I_INITIAL_A = 5.0       # Initial Thyristor Current = 5 Amperes (from Q55)

# Calculate resonant angular frequency (omega_0)
# omega_0 = 1 / sqrt(L * C)
omega0 = 1.0 / math.sqrt(L_VALUE_H * C_VALUE_F)

# Calculate the peak commutation current (I_peak_commutation)
# I_peak_commutation = Vs * sqrt(C / L)
i_peak_commutation = VS_VALUE_V * math.sqrt(C_VALUE_F / L_VALUE_H)

print("Circuit Parameters:")
print(f"  Inductance (L): {L_VALUE_H:.2e} H")
print(f"  Capacitance (C): {C_VALUE_F:.2e} F")
print(f"  Source Voltage (Vs): {VS_VALUE_V:.1f} V")
print(f"  Initial Thyristor Current (I_initial): {I_INITIAL_A:.1f} A\n")

print(f"Calculated Resonant Angular Frequency (omega_0): {omega0:.2f} rad/s")
print(f"Calculated Peak Commutation Current: {i_peak_commutation:.2f} A")

# Check if commutation is possible (peak commutation current must be >= initial current)
if i_peak_commutation < I_INITIAL_A:
    print(f"Error: Commutation not possible. Peak commutation current ({i_peak_commutation:.2f} A) is less than initial current ({I_INITIAL_A:.2f} A).")
else:
    # Calculate the argument for asin: sin(omega_0 * t) = I_initial / I_peak_commutation
    sin_arg = I_INITIAL_A / i_peak_commutation

    # Calculate the angle (omega_0 * t) using asin
    # The thyristor turns off when the commutation current equals the initial current.
    # This happens at the first positive time 't' where i(t) = I_initial.
    angle = math.asin(sin_arg)

    # Calculate the time to turn off
    # t = angle / omega_0
    time_to_turn_off_s = angle / omega0

    print(f"\nTime taken for the device to turn off: {time_to_turn_off_s:.2e} seconds ({time_to_turn_off_s * 1e6:.2f} microseconds)")

