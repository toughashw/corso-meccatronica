const int fotointerruttore = 7;
const int led = 12;
// dichiaro i PINS di Ingressi ed Uscite

void setup () {
pinMode(fotointerruttore, INPUT);
pinMode(led, OUTPUT);
}
// definisco tramite la PinMode chi è INPUT e chi OUTPUT

void loop () {
boolean statoint = digitalRead(fotointerruttore);
Serial.println("Lo stato del foto interruttore è: ",statoint);
// leggo tramite la digitalRead il valore booleano (0/1) del fotointerruttore

if (statoint == HIGH) {
    digitalWrite(led, LOW)
}
// se è HIGH(1) il fotointerruttore si comporta come un circuito aperto e di conseguenza il led non si accenderà per mancato passaggio di corrente
else {
    digitalWrite(led,HIGH)
}
// else (altrimenti) lo statoint sarà a LOW e di conseguenza il led si accenderà
}