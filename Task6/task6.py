import numpy as np

def calculate_lc_current(L_mH, C_microF, Vc0):
    """
    Calculates the current in an LC circuit at time t.

    Args:
        L_mH (float): Inductance in millihenries (mH).
        C_microF (float): Capacitance in microfarads (uF).
        Vc0 (float): Initial capacitor voltage in volts (V).

    Returns:
        tuple: A tuple containing:
               - omega_0 (float): Angular resonant frequency in rad/s.
               - A (float): Amplitude of charge (related to initial charge).
               - B (float): Another constant for charge (zero for this initial condition).
               - current_formula_str (str): A string representation of the current formula I(t).
               - options (dict): A dictionary of the given options.
               - calculated_current_amplitude (float): The amplitude of the calculated current.
               - calculated_omega_t (float): The angular frequency term for the calculated current.
    """

    # Convert L to Henries
    L = L_mH * 1e-3
    # Convert C to Farads
    C = C_microF * 1e-6

    # Calculate angular resonant frequency (omega_0)
    omega_0 = 1 / np.sqrt(L * C)

    # Initial conditions:
    # I(0) = 0
    # Vc(0) = Vc0

    # From I(t) = dQ/dt = -A*omega_0*sin(omega_0*t) + B*omega_0*cos(omega_0*t)
    # I(0) = B*omega_0 = 0 => B = 0

    # Q(t) = A*cos(omega_0*t) + B*sin(omega_0*t)
    # With B=0, Q(t) = A*cos(omega_0*t)

    # Vc(t) = Q(t) / C
    # Vc(0) = Q(0) / C = A / C
    # A = Vc0 * C

    # Re-evaluating A based on the convention that current 'i' is flowing out of the positively charged plate
    # If the bottom plate is at +100V, and current 'i' is shown leaving the top plate,
    # then the charge Q on the top plate is initially negative, so V_C = (Q_bottom - Q_top)/C = (-Q_top)/C
    # Or, if Q is the charge on the plate connected to the inductor where current enters from,
    # and Vc is defined as voltage across capacitor from top to bottom, then Vc = Q_top / C.
    # From the diagram, Vc is across the capacitor with '+' at the bottom.
    # So, Vc = V_bottom - V_top = Q_bottom / C.
    # Initial charge on bottom plate Q_bottom(0) = C * Vc0
    # Q(t) here represents charge on the capacitor plate where the current 'i' flows *into*.
    # In the diagram, 'i' flows into the top plate. Let Q be the charge on the top plate.
    # Then Vc = V_bottom - V_top. If V_bottom is positive, V_top is negative.
    # So Q_top is negative. Vc = Q_bottom / C = -Q_top / C.
    # So Q_top(0) = -Vc0 * C

    # Let's stick to the convention where I = dQ/dt and Vc = Q/C.
    # If Vc(0) = 100V and the positive terminal is at the bottom, then the charge on the bottom plate is +Q_0.
    # The charge on the top plate is -Q_0.
    # If current 'i' flows clockwise (as indicated), it means positive charge is flowing out of the bottom plate
    # and into the top plate (from the inductor side).
    # Let Q be the charge on the plate where current 'i' flows *into* (the top plate).
    # Then V_top - V_bottom = Q/C. So V_bottom - V_top = -Q/C.
    # Given Vc(0) = 100V across the capacitor with + at the bottom, so V_bottom - V_top = 100V.
    # So, 100 = -Q(0)/C => Q(0) = -100 * C = -Vc0 * C.
    # Thus, Q(0) = -Vc0 * C.
    # From Q(t) = A*cos(omega_0*t) + B*sin(omega_0*t),
    # Q(0) = A.
    # So, A = -Vc0 * C

    # With A = -Vc0 * C and B = 0
    # A = -(100 V) * (10 * 10^-6 F) = -1 * 10^-3 C

    # The current I(t) = dQ/dt = -A * omega_0 * sin(omega_0 * t)
    A_charge = -Vc0 * C
    current_amplitude = -A_charge * omega_0

    current_formula_str = f"{current_amplitude:.0f}*sin({omega_0:.0f}*t) A"
    # Note: if current_amplitude is negative, the string will correctly show e.g., -10*sin(...)

    options = {
        'A': "5*cos(5*10^3*t) A",
        'B': "5*sin(10^4*t) A",
        'C': "10*cos(5*10^3*t) A",
        'D': "10*sin(10^4*t) A"
    }

    return omega_0, A_charge, 0, current_formula_str, options, current_amplitude, omega_0

# Given values
L_mH = 1
C_microF = 10
Vc0 = 100

omega_0, A_charge, B_charge, current_formula_str, options, calculated_current_amplitude, calculated_omega_t = calculate_lc_current(L_mH, C_microF, Vc0)

print(f"Given L = {L_mH} mH, C = {C_microF} µF, Initial Vc = {Vc0} V")
print(f"Calculated Angular Resonant Frequency (omega_0): {omega_0:.0f} rad/s")
print(f"Calculated A (charge amplitude): {A_charge:.3e} C")
print(f"Calculated B (charge amplitude): {B_charge} C")
print(f"The current I(t) through the circuit is: {current_formula_str}")
print("\nOptions:")
for key, value in options.items():
    print(f"({key}) {value}")

print("\nMatching with options:")
# Check if the calculated amplitude and omega_0 match any option
# We expect current to be of the form A_I * sin(omega_0 * t)
# The amplitude is 10, and omega_0 is 10^4.
# So, the target option is 10*sin(10^4*t) A

if abs(calculated_current_amplitude - 10) < 1e-9 and abs(calculated_omega_t - 10000) < 1e-9:
    print("The calculated current matches option (D): 10sin(10^4 t) A")
elif abs(calculated_current_amplitude - 5) < 1e-9 and abs(calculated_omega_t - 10000) < 1e-9:
    print("The calculated current matches option (B): 5sin(10^4 t) A")
else:
    print("The calculated current does not directly match the provided options in exact form.")
    print(f"Calculated amplitude: {calculated_current_amplitude:.0f}")
    print(f"Calculated angular frequency: {calculated_omega_t:.0f}")
