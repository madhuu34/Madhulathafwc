#include <LiquidCrystal.h>

LiquidCrystal lcd(12,11,5,4,3,2);

int V_out_q = 0;
float V_in = 5, V_out;
float R1 = 220, R2;

void setup(){
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.print(".  OMM MAHAPRANA DEEPAM SHIVAM SHIVAM");
  for (int i = 0; ; i++) {  // Adjust according to text length
        lcd.scrollDisplayLeft();
        delay(500);  // Adjust speed of scrolling
    }
  
  Serial.begin(9600);
}

void loop(){
  V_out_q = analogRead(0);
  V_out = V_in * V_out_q / 1024;
  R2 = R1 * ((V_in)/(V_out)-1.0);
  delay(3000);
  Serial.println(R2);
  lcd.setCursor(0,1);
  lcd.print("R = ");
  lcd.print(R2);
  lcd.print(" Ohm");
}