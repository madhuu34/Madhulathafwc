from machine import Pin, PWM
import time
import math

# Setup
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
led = PWM(Pin(15))
led.freq(1000)  # PWM frequency

started = False
start_time = 0

while True:
    if button.value() and not started:
        start_time = time.ticks_ms()
        started = True

    if started:
        t_ms = time.ticks_ms() - start_time
        t_sec = t_ms / 1000.0

        # Simulate i(t) = 10 * sin(10^4 * t)
        i = 10 * math.sin(10000 * t_sec)  # theoretical current

        # Normalize to 0-65535 for PWM duty cycle
        duty = int((i + 10) / 20 * 65535)
        led.duty_u16(duty)
    else:
        led.duty_u16(0)
    
    time.sleep(0.01)