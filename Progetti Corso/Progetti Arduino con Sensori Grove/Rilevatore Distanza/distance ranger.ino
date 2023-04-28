#include <Ultrasonic.h>
#include <rgb_lcd.h>
#include <Wire.h>

Ultrasonic sensore(4);
rgb_lcd lcd;

const int ledred = 5;
const int ledgreen = 6;
const int ledblue = 7;
const int buzzer = 8;

const int lcdR = 226;
const int lcdG = 168;
const int lcdB = 65;

void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.setRGB(lcdR,lcdG, lcdB);
  pinMode(ledred, OUTPUT);
  pinMode(ledgreen, OUTPUT);
  pinMode(ledblue, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  float distanzaincm = sensore.MeasureInCentimeters();
  Serial.print(distanzaincm);
  Serial.print(" cm");
  lcd.setCursor(0,0);
  lcd.print("La distanza e': ");
  lcd.setCursor(5,1);
  lcd.print(distanzaincm);
  lcd.setCursor(11,1);
  lcd.print("cm");

  if (distanzaincm >0.0 && distanzaincm <=10.0) {
  lcd.blinkLED();
  lcd.setRGB(255, 0, 0);
  digitalWrite(ledred, HIGH);
  digitalWrite(ledgreen, LOW);
  digitalWrite(ledblue, LOW);
  digitalWrite(buzzer, HIGH);
  }

  if (distanzaincm >10.0 && distanzaincm <=20.0) {
  lcd.blinkLED();
  lcd.setRGB(0, 255, 0);
  digitalWrite(ledred, LOW);
  digitalWrite(ledgreen, HIGH);
  digitalWrite(ledblue, LOW);
  digitalWrite(buzzer, HIGH);
  }
  
  if (distanzaincm >20.0 && distanzaincm <30.0) {
  lcd.blinkLED();
  lcd.setRGB(0, 0, 255);
  digitalWrite(ledred, LOW);
  digitalWrite(ledgreen, LOW);
  digitalWrite(ledblue, HIGH);
  digitalWrite(buzzer, HIGH);
  }

if (distanzaincm >=30.0) {
  lcd.blinkLED();
  lcd.setRGB(255, 255, 255);
  lcd.print("Sono fuori range");
  }
}