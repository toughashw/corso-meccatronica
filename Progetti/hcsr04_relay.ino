const int trigPin = 9;
const int echoPin = 10;
const int relay = 12;

long durata_impulso;
long distanza;

void setup() {
pinMode(trigPin, OUTPUT); 
pinMode(echoPin, INPUT);
pinMode(relay, OUTPUT);
Serial.begin(9600); 
}

void loop() {
digitalWrite(trigPin, LOW);
delayMicroseconds(2);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

durata_impulso = pulseIn(echoPin, HIGH);

distanza= durata_impulso*0.034/2;

Serial.print("Distanza: ");
Serial.println(distanza);
if (distanza <= 10.0) {
    digitalWrite(relay,HIGH);
}
else {
    digitalWrite(relay,LOW);
}
}