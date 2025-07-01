#include <stdio.h>   // Required for printf
#include <stdbool.h> // Required for bool, true, false

// Function F derived from the K-map: F = X'Z + YZ
// In C, '!' is NOT, '&&' is AND, '||' is OR
bool target_function_F(bool X, bool Y, bool Z) {
    bool not_X = !X;
    bool term1 = not_X && Z;
    bool term2 = Y && Z;
    return term1 || term2;
}

// Circuit A: F_A = XY + YZ
bool circuit_A(bool X, bool Y, bool Z) {
    bool term1 = X && Y;
    bool term2 = Y && Z;
    return term1 || term2;
}

// Circuit B: F_B = (X.Y)' + (Y.Z)' (NAND outputs ORed)
// De Morgan's Theorem: (A.B)' = A' + B'
// So, (X.Y)' = X' + Y'
// And, (Y.Z)' = Y' + Z'
// F_B = (X' + Y') + (Y' + Z') = X' + Y' + Z'
bool circuit_B(bool X, bool Y, bool Z) {
    bool nand1_out = !(X && Y); // Equivalent to (X and Y) with NOT
    bool nand2_out = !(Y && Z); // Equivalent to (Y and Z) with NOT
    return nand1_out || nand2_out;
}

// Circuit C: F_C = X'Y + YZ
bool circuit_C(bool X, bool Y, bool Z) {
    bool not_X = !X;
    bool term1 = not_X && Y;
    bool term2 = Y && Z;
    return term1 || term2;
}

// Circuit D: This function directly implements the gate logic described in the Python code.
// F_D = ( (X.Y)' . Z )' + ( (Y.Z)' . X )'
bool circuit_D(bool X, bool Y, bool Z) {
    bool top_left_nand_out = !(X && Y);
    bool bottom_left_nand_out = !(Y && Z);

    bool top_right_nand_input_1 = top_left_nand_out;
    bool top_right_nand_input_2 = Z;
    bool top_right_nand_out = !(top_right_nand_input_1 && top_right_nand_input_2);

    bool bottom_right_nand_input_1 = bottom_left_nand_out;
    bool bottom_right_nand_input_2 = X;
    bool bottom_right_nand_out = !(bottom_right_nand_input_1 && bottom_right_nand_input_2);

    bool final_or_out = top_right_nand_out || bottom_right_nand_out;
    return final_or_out;
}

int main() {
    // Test all 8 possible input combinations
    printf("Truth Table Comparison:\n");
    printf("X Y Z | F_Target | F_A | F_B | F_C | F_D | Match A | Match B | Match C | Match D\n");
    printf("-------------------------------------------------------------------------------------\n");

    // To track which circuits match for ALL inputs
    bool matches_A = true;
    bool matches_B = true;
    bool matches_C = true;
    bool matches_D = true;

    // Loop through all 8 combinations of X, Y, Z (000 to 111)
    for (int X_int = 0; X_int <= 1; X_int++) {
        for (int Y_int = 0; Y_int <= 1; Y_int++) {
            // THIS WAS THE LINE WITH THE ERROR IN YOUR PREVIOUS ATTEMPT
            // It should be 'Z_int++' and then a closing parenthesis ')'
            for (int Z_int = 0; Z_int <= 1; Z_int++) {
                // Convert int to bool for function calls
                bool X = (bool)X_int;
                bool Y = (bool)Y_int;
                bool Z = (bool)Z_int;

                bool f_target = target_function_F(X, Y, Z);
                bool f_a = circuit_A(X, Y, Z);
                bool f_b = circuit_B(X, Y, Z);
                bool f_c = circuit_C(X, Y, Z);
                bool f_d = circuit_D(X, Y, Z);

                // Determine row-wise match status
                const char* match_a_row = f_target == f_a ? "YES" : "NO ";
                const char* match_b_row = f_target == f_b ? "YES" : "NO ";
                const char* match_c_row = f_target == f_c ? "YES" : "NO ";
                const char* match_d_row = f_target == f_d ? "YES" : "NO ";

                // Print the current row of the truth table
                printf("%d %d %d | %d          | %d   | %d   | %d   | %d   | %s      | %s      | %s      | %s\n",
                       X_int, Y_int, Z_int, (int)f_target, (int)f_a, (int)f_b, (int)f_c, (int)f_d,
                       match_a_row, match_b_row, match_c_row, match_d_row);

                // Update overall match status
                if (f_target != f_a) matches_A = false;
                if (f_target != f_b) matches_B = false;
                if (f_target != f_c) matches_C = false;
                if (f_target != f_d) matches_D = false;
            } // Closes Z_int loop
        } // Closes Y_int loop
    } // Closes X_int loop

    printf("\n--- Summary ---\n");
    printf("Circuit A matches F: %s\n", matches_A ? "YES" : "NO");
    printf("Circuit B matches F: %s\n", matches_B ? "YES" : "NO");
    printf("Circuit C matches F: %s\n", matches_C ? "YES" : "NO");
    printf("Circuit D matches F: %s\n", matches_D ? "YES" : "NO");

    return 0; // Indicate successful execution
}
