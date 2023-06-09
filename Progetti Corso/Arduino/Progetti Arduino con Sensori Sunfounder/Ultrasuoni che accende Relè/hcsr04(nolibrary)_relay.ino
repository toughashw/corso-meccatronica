const int trigPin = 9;
const int echoPin = 10;
const int relay = 12;

long durata_impulso;
float distanza;

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

distanza=durata_impulso*0.034/2;
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