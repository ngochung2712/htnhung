#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 20, 4);

void setup() {
  // put your setup code here, to run once:
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  float val=analogRead(A1)*(5.0/1023.0);
  delay(25);
  lcd.setCursor(0, 0);
  lcd.print(val);
  Serial.println(val);
}
