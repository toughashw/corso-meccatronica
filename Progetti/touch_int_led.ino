const int touchint = 7;
const int led = 12;
// dichiaro i PINS di Ingressi ed Uscite

void setup () {
pinMode(touchint, INPUT);
pinMode(led, OUTPUT);
Serial.begin(9600);
}
// definisco tramite la PinMode chi è INPUT e chi OUTPUT

void loop () {
boolean statoint = digitalRead(touchint);
Serial.println("Lo stato dell'interruttore touch è: ",statoint);
// leggo tramite la digitalRead lo stato dell'interruttore touch

if (statoint == HIGH) {
    digitalWrite(led, LOW)
}
// se è HIGH(1) il fotointerruttore si comporta come un circuito aperto e di conseguenza il led non si accenderà per mancato passaggio di corrente
else {
    digitalWrite(led,HIGH)
}
// else (altrimenti) lo statoint sarà a LOW e di conseguenza il led si accenderà