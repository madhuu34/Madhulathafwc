from machine import Pin
import time

# Define pushbuttons as inputs with pull-down configuration
X = Pin(14, Pin.IN, Pin.PULL_DOWN)
Y = Pin(15, Pin.IN, Pin.PULL_DOWN)
Z = Pin(16, Pin.IN, Pin.PULL_DOWN)

# Define output LED pin
F = Pin(17, Pin.OUT)

while True:
    x_val = X.value()
    y_val = Y.value()
    z_val = Z.value()

    # Logic implementation: F = (X AND Y) OR (Y AND Z)
    output = (x_val and y_val) or (y_val and z_val)

    F.value(output)

    # Optional: print status for debugging
    print(f"X: {x_val}, Y: {y_val}, Z: {z_val}, F: {output}")
    
    time.sleep(0.1)
