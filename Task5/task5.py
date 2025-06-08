# Function F derived from the K-map: F = X'Z + YZ
def target_function_F(X, Y, Z):
    not_X = not X
    term1 = not_X and Z
    term2 = Y and Z
    return term1 or term2

# Circuit A: F_A = XY + YZ
def circuit_A(X, Y, Z):
    term1 = X and Y
    term2 = Y and Z
    return term1 or term2

# Circuit B: F_B = X' + Y' + Z' (assuming the ambiguous box is a buffer for X)
# Alternative interpretation: F_B = X + Y' + Z' (if box is inverter)
# We will use the former for this comparison, as typically simpler interpretations are preferred unless specified.
# Let's write the circuit function based on its gates as derived: F_B = (X.Y)' + (Y.Z)'
def circuit_B(X, Y, Z):
    nand1_out = not (X and Y)
    nand2_out = not (Y and Z)
    return nand1_out or nand2_out

# Circuit C: F_C = X'Y + YZ
def circuit_C(X, Y, Z):
    not_X = not X # Equivalent to not (X and X)
    term1 = not_X and Y
    term2 = Y and Z
    return term1 or term2

# Circuit D: F_D = XY + YZ + X' + Z'
def circuit_D(X, Y, Z):
    top_left_nand_out = not (X and Y)
    bottom_left_nand_out = not (Y and Z)
    
    top_right_nand_input_1 = top_left_nand_out
    top_right_nand_input_2 = Z
    top_right_nand_out = not (top_right_nand_input_1 and top_right_nand_input_2)
    
    bottom_right_nand_input_1 = bottom_left_nand_out
    bottom_right_nand_input_2 = X
    bottom_right_nand_out = not (bottom_right_nand_input_1 and bottom_right_nand_input_2)
    
    final_or_out = top_right_nand_out or bottom_right_nand_out
    return final_or_out

# Test all 8 possible input combinations
print("Truth Table Comparison:")
print("X Y Z | F_Target | F_A | F_B | F_C | F_D | Match A | Match B | Match C | Match D")
print("-------------------------------------------------------------------------------------")

# To track which circuits match for ALL inputs
matches_A = True
matches_B = True
matches_C = True
matches_D = True

for X in [0, 1]:
    for Y in [0, 1]:
        for Z in [0, 1]:
            f_target = target_function_F(X, Y, Z)
            f_a = circuit_A(X, Y, Z)
            f_b = circuit_B(X, Y, Z)
            f_c = circuit_C(X, Y, Z)
            f_d = circuit_D(X, Y, Z)
            
            match_a_row = "YES" if f_target == f_a else "NO "
            match_b_row = "YES" if f_target == f_b else "NO "
            match_c_row = "YES" if f_target == f_c else "NO "
            match_d_row = "YES" if f_target == f_d else "NO "
            
            print(f"{X} {Y} {Z} | {int(f_target)}        | {int(f_a)}   | {int(f_b)}   | {int(f_c)}   | {int(f_d)}   | {match_a_row}     | {match_b_row}     | {match_c_row}     | {match_d_row}")
            
            if f_target != f_a: matches_A = False
            if f_target != f_b: matches_B = False
            if f_target != f_c: matches_C = False
            if f_target != f_d: matches_D = False

print("\n--- Summary ---")
print(f"Circuit A matches F: {'YES' if matches_A else 'NO'}")
print(f"Circuit B matches F: {'YES' if matches_B else 'NO'}")
print(f"Circuit C matches F: {'YES' if matches_C else 'NO'}")
print(f"Circuit D matches F: {'YES' if matches_D else 'NO'}")
