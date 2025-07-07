#include <stdio.h>
#include <math.h>

// Define constants for the circuit using values from Q54
#define L_VALUE_H 1.0e-3      // Inductance L = 1 mH = 1 * 10^-3 Henry
#define C_VALUE_F 10.0e-6     // Capacitance C = 10 uF = 10 * 10^-6 Farad
#define VS_VALUE_V 100.0      // Source Voltage Vs = 100 Volts (from Q55)
#define I_INITIAL_A 5.0       // Initial Thyristor Current = 5 Amperes (from Q55)
#define PI M_PI               // Pi constant from math.h

int main() {
    // Calculate resonant angular frequency (omega_0)
    // omega_0 = 1 / sqrt(L * C)
    double omega0 = 1.0 / sqrt(L_VALUE_H * C_VALUE_F);

    // Calculate the peak commutation current (I_peak_commutation)
    // I_peak_commutation = Vs * sqrt(C / L)
    double i_peak_commutation = VS_VALUE_V * sqrt(C_VALUE_F / L_VALUE_H);

    printf("Circuit Parameters:\n");
    printf("  Inductance (L): %.2e H\n", L_VALUE_H);
    printf("  Capacitance (C): %.2e F\n", C_VALUE_F);
    printf("  Source Voltage (Vs): %.1f V\n", VS_VALUE_V);
    printf("  Initial Thyristor Current (I_initial): %.1f A\n\n", I_INITIAL_A);

    printf("Calculated Resonant Angular Frequency (omega_0): %.2f rad/s\n", omega0);
    printf("Calculated Peak Commutation Current: %.2f A\n", i_peak_commutation);

    // Check if commutation is possible (peak commutation current must be >= initial current)
    if (i_peak_commutation < I_INITIAL_A) {
        printf("Error: Commutation not possible. Peak commutation current (%.2f A) is less than initial current (%.2f A).\n", i_peak_commutation, I_INITIAL_A);
        return 1; // Exit with error
    }

    // Calculate the argument for arcsin: sin(omega_0 * t) = I_initial / I_peak_commutation
    double sin_arg = I_INITIAL_A / i_peak_commutation;

    // Calculate the angle (omega_0 * t) using arcsin
    // The thyristor turns off when the commutation current equals the initial current.
    // This happens at the first positive time 't' where i(t) = I_initial.
    double angle = asin(sin_arg);

    // Calculate the time to turn off
    // t = angle / omega_0
    double time_to_turn_off_s = angle / omega0;

    printf("\nTime taken for the device to turn off: %.2e seconds (%.2f microseconds)\n", time_to_turn_off_s, time_to_turn_off_s * 1e6);

    return 0;
}

