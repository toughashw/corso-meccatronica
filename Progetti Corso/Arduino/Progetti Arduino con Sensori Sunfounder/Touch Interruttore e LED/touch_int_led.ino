const int touchint = 7;
const int led = 12;
// dichiaro i PINS di Ingressi ed Uscite

void setup () {
pinMode(touchint, INPUT);
pinMode(led, OUTPUT);
}
// definisco tramite la PinMode chi è INPUT e chi OUTPUT

void loop () {
boolean statoint = digitalRead(touchint);
// leggo tramite la digitalRead lo stato dell'interruttore touch

if (statoint == HIGH) {
    digitalWrite(led, HIGH);
}
// se è HIGH(1) il fotointerruttore si comporta come un circuito aperto e di conseguenza il led non si accenderà per mancato passaggio di corrente
delay(1000);
else {
    digitalWrite(led,LOW);
}
// else (altrimenti) lo statoint sarà a LOW e di conseguenza il led si accenderà
}