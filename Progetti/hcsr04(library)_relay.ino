#include <HCSR04.h>

const byte triggerPin = 9;
const byte echoPin = 10;
const int relay = 12;
unsigned short maxDistanceCm = 100;
UltraSonicDistanceSensor distanceSensor(triggerPin, echoPin, maxDistanceCm);

void setup() {
Serial.begin(9600); 
pinMode(relay, OUTPUT);
}

void loop() {
float distanza = distanceSensor.measureDistanceCm();
int pos;
for (pos=0; pos<29; pos++)
{
Serial.print("Distanza: ");
Serial.print(distanza);
Serial.println(" cm");
}
if (distanza <= 10.00) {
    digitalWrite(relay,HIGH);
}
else {
    digitalWrite(relay,LOW);
}
}
