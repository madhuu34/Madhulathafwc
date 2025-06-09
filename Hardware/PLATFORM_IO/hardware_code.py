from machine import Pin
import time

def get_kmap_input():
    print("Enter values for the 2x4 K-map (0 or 1 only):")
    print("Follow this minterm order: m0 m1 m3 m2 m4 m5 m7 m6")
    minterm_order = [0, 1, 3, 2, 4, 5, 7, 6]
    kmap = [0] * 8
    for idx in minterm_order:
        while True:
            val = input(f"Enter value for m{idx} (0 or 1): ").strip()
            if val in ['0', '1']:
                kmap[idx] = int(val)
                break
            else:
                print("Invalid input. Please enter 0 or 1.")
    return kmap

def print_kmap(kmap):
    print("\nK-map (X vs YZ):")
    print("        YZ")
    print("       00  01  11  10")
    print("X=0:  {}   {}   {}   {}".format(kmap[0], kmap[1], kmap[3], kmap[2]))
    print("X=1:  {}   {}   {}   {}".format(kmap[4], kmap[5], kmap[7], kmap[6]))

def get_index(x, y, z):
    """Return index into kmap given binary inputs"""
    return (x << 2) | (y << 1) | z

# K-map input and display
kmap = get_kmap_input()
print_kmap(kmap)

# Initialize pins
X = Pin(14, Pin.IN, Pin.PULL_DOWN)
Y = Pin(15, Pin.IN, Pin.PULL_DOWN)
Z = Pin(16, Pin.IN, Pin.PULL_DOWN)
F = Pin(13, Pin.OUT)

print("\nReady. Press input switches to test the K-map logic (F will light LED).")

prev_state = (-1, -1, -1)  # For detecting state change

while True:
    x_val = X.value()
    y_val = Y.value()
    z_val = Z.value()
    current_state = (x_val, y_val, z_val)

    if current_state != prev_state:
        index = get_index(x_val, y_val, z_val)
        output = kmap[index]
        F.value(output)
        print(f"X={x_val}, Y={y_val}, Z={z_val} => F={output}")
        prev_state = current_state

    time.sleep(0.1)
