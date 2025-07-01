#include <stdio.h>   // For printf, sprintf
#include <math.h>    // For sqrt, sin, fabs
#include <string.h>  // For strcmp (if needed for string matching)
#include <stdbool.h> // For bool type

// Function to calculate LC circuit parameters and current formula
// Returns are passed by reference for multiple return values
void calculate_lc_current(double L_mH, double C_microF, double Vc0,
                          double *omega_0_ptr, double *A_charge_ptr,
                          char *current_formula_str, int current_formula_str_len,
                          double *calculated_current_amplitude_ptr,
                          double *calculated_omega_t_ptr) {

    // Convert L to Henries
    double L = L_mH * 1e-3;
    // Convert C to Farads
    double C = C_microF * 1e-6;

    // Calculate angular resonant frequency (omega_0)
    *omega_0_ptr = 1.0 / sqrt(L * C);

    // Initial conditions:
    // I(0) = 0
    // Vc(0) = Vc0 (positive terminal at bottom, current 'i' flows into top)
    // Q(t) here represents charge on the capacitor plate where the current 'i' flows *into*.
    // V_top - V_bottom = Q/C. Given Vc(0) = V_bottom - V_top = Vc0.
    // So, Vc0 = -Q(0)/C => Q(0) = -Vc0 * C.
    // From Q(t) = A*cos(omega_0*t) + B*sin(omega_0*t),
    // Q(0) = A.
    // So, A = -Vc0 * C

    // With A = -Vc0 * C and B = 0 (since I(0) = 0)
    *A_charge_ptr = -Vc0 * C;

    // The current I(t) = dQ/dt = -A * omega_0 * sin(omega_0 * t)
    *calculated_current_amplitude_ptr = -(*A_charge_ptr) * (*omega_0_ptr);
    *calculated_omega_t_ptr = *omega_0_ptr;

    // Format the current formula string
    snprintf(current_formula_str, current_formula_str_len,
             "%.0f*sin(%.0f*t) A", *calculated_current_amplitude_ptr, *calculated_omega_t_ptr);
}

int main() { // <-- MAKE SURE THIS OPENING BRACE IS PRESENT
    // Given values
    double L_mH = 1.0;
    double C_microF = 10.0;
    double Vc0 = 100.0;

    double omega_0;
    double A_charge;
    double calculated_current_amplitude;
    double calculated_omega_t;
    char current_formula_str[100]; // Buffer for the formula string

    // Call the function to calculate parameters
    calculate_lc_current(L_mH, C_microF, Vc0,
                         &omega_0, &A_charge,
                         current_formula_str, sizeof(current_formula_str),
                         &calculated_current_amplitude, &calculated_omega_t);

    // Corrected line 62: Replaced hex escape for µ with just "uF" for simplicity and wider compatibility.
    // If you absolutely need 'µ' and your system supports UTF-8, ensure your source file is saved as UTF-8
    // and compile with `gcc -finput-charset=UTF-8 -fexec-charset=UTF-8 lc_circuit.c -o lc_circuit -lm`
    printf("Given L = %.0f mH, C = %.0f uF, Initial Vc = %.0f V\n", L_mH, C_microF, Vc0);
    printf("Calculated Angular Resonant Frequency (omega_0): %.0f rad/s\n", omega_0);
    printf("Calculated A (charge amplitude): %.3e C\n", A_charge);
    printf("Calculated B (charge amplitude): 0.0 C\n"); // B is always 0 for I(0) = 0
    printf("The current I(t) through the circuit is: %s\n", current_formula_str);

    // Define options (as arrays of strings for clarity)
    const char* options_keys[] = {"A", "B", "C", "D"};
    const char* options_values[] = {
        "5*cos(5*10^3*t) A",
        "5*sin(10^4*t) A",
        "10*cos(5*10^3*t) A",
        "10*sin(10^4*t) A"
    };
    int num_options = sizeof(options_keys) / sizeof(options_keys[0]);

    printf("\nOptions:\n");
    for (int i = 0; i < num_options; i++) {
        printf("(%s) %s\n", options_keys[i], options_values[i]);
    }

    printf("\nMatching with options:\n"); // <-- This is line 83 in my current numbering
    // Check if the calculated amplitude and omega_0 match any option
    // We expect current to be of the form A_I * sin(omega_0 * t)
    // The amplitude is 10, and omega_0 is 10^4.
    // So, the target option is 10*sin(10^4*t) A

    // Using a small epsilon for floating point comparison
    double epsilon = 1e-9;

    if (fabs(calculated_current_amplitude - 10.0) < epsilon && fabs(calculated_omega_t - 10000.0) < epsilon) {
        printf("The calculated current matches option (D): %s\n", options_values[3]); // Index 3 for option D
    } else if (fabs(calculated_current_amplitude - 5.0) < epsilon && fabs(calculated_omega_t - 10000.0) < epsilon) {
        printf("The calculated current matches option (B): %s\n", options_values[1]); // Index 1 for option B
    } else {
        printf("The calculated current does not directly match the provided options in exact form.\n");
        printf("Calculated amplitude: %.0f\n", calculated_current_amplitude);
        printf("Calculated angular frequency: %.0f\n", calculated_omega_t);
    }

    return 0;
} // <-- MAKE SURE THIS CLOSING BRACE IS PRESENT AT THE VERY END OF THE FILE
