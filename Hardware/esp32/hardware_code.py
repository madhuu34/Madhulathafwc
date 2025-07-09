// Simulating i(t) = 5 cos(5000 t)
// Use PWM to fade LED from max to off over ~314 µs

#define NUM_SAMPLES 100
const int outputPin = 9;
int waveTable[NUM_SAMPLES];

void setup() {
  // Generate cosine waveform samples scaled to 0–255 (for analogWrite)
  for (int i = 0; i < NUM_SAMPLES; i++) {
    waveTable[i] = 127 + 127 * cos(PI * i / (2.0 * NUM_SAMPLES));  // 0 to 255
  }
}

void loop() {
  // Simulate only one thyristor turn-off pulse
  for (int i = 0; i < NUM_SAMPLES; i++) {
    analogWrite(outputPin, waveTable[i]);
    delayMicroseconds(3); // Total time ~300 µs
  }
  analogWrite(outputPin, 0);  // Ensure OFF
  delay(1000); // Wait before repeating
}
