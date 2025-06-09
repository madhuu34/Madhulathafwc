# Step 1: Define minterms based on the K-map
# From the image: 1s at cell positions:
# (X=0, YZ=01) → minterm 1
# (X=0, YZ=11) → minterm 3
# (X=1, YZ=11) → minterm 7
minterms = [1, 3, 7]
# Step 2: Manually deduce minimal expression from K-map analysis
# Grouping:
# - Minterm 1 (001): X=0, Y=0, Z=1 → X̅Y̅
# - Minterm 3 and 7 (011, 111): Y=1, Z=1 → YZ

# Final minimized expression: F = X̅Y̅ + YZ
derived_expression = "X̅Y̅ + YZ"

# Step 3: Define the options
options = {
    "A": "X̅Y + YZ",
    "B": "X̅Y̅ + YZ",
    "C": "X̅Y̅ + YZ̅",
    "D": "X̅Y̅ + Y̅Z"
}

# Step 4: Compare and find the correct option
correct_option = None
for opt, expr in options.items():
    if expr.replace(" ", "") == derived_expression.replace(" ", ""):
        correct_option = opt
        break

# Step 5: Print result and explanation
print(f"Correct Option: ({correct_option})")
print(f"Minimized Expression: {derived_expression}")
print("\nExplanation:")
print(f"""
From the K-map:
- 1s are at minterms: 1 (001), 3 (011), and 7 (111)

Groupings:
- Minterm 1: X=0, Y=0 → X̅Y̅
- Minterms 3 and 7: Y=1, Z=1 → YZ

Therefore, minimized Boolean expression is:
F = X̅Y̅ + YZ

Which matches option ({correct_option}): {options[correct_option]}
""")
