# Corso di Meccatronica
Repository del Corso di Meccatronica della Regione Puglia

- LIBRERIE
```
#include <nomelibreria.h>
```

- TIPI DI DATI
```
INTERO --> int
DECIMALE --> float
A DOPPIA PRECISIONE --> double
INTERI CON SEGNO --> long
BOOLEANO --> boolean
CARATTERE --> char
STRINGA --> char(i)
```

- DICHIARIAZIONE PINS
```
const int nomePin = numeroPin;
#define nomePin numeroPin;
```

- DICHIARIAZIONE INGRESSI/USCITE
```
void setup() {
pinMode(nomePin/numeroPin,INPUT/OUTPUT);
}
```

- LETTURA/SCRITTURA DA INGRESSI ANALOGICI/DIGITALI
```
void loop() {
digitalRead(nomePin/numeroPin);
digitalWrite(nomePin/numeroPin, HIGH/LOW);
analogRead(nomePin/numeroPin);
analogWrite(nomePin/numeroPin,0-255);
}
```

- OPERAZIONI CON SERIALE
```
void setup() {
Serial.begin(9600); --> Legge da Seriale con baund a 9600
}
void loop() {
Serial.print("TESTO"); --> Stampa su monitor seriale una stringa di testo
Serial.print(dati);    --> Stampa su monitor seriale lo stream di dati
Serial.println("TESTO"); --> Stampa a capo su monitor seriale una stringa di testo
Serial.println(dati);  --> Stampa a capo su monitor seriale lo stream di dati
}
```

- OPERAZIONI CON LCD DISPLAY
```
void setup() {
lcd.begin(16,2); --> Inizializzazione del display a 16 righe e 2 colonne
}
void loop() {
lcd.setRGB (ColorR, ColorG, ColorB); --> imposta la retroilluminazione del colore prescelto
lcd.setCursor(posizioneriga,posizionecolonna); --> Imposta il cursore sulla posizione prescelta
lcd.clear(); --> pulisce il contenuto del display
lcd.noDisplay(); --> Spegne il Display
lcd.blinkLED(); --> fa lampeggiare il display
lcd.print("TESTO"); --> Stampa su display una stringa di testo
lcd.print(dati); --> Stampa su display lo stream di dati
}
```

- OPERATORI MATEMATICI E LOGICI
```
ASSEGNAZIONE --> =
MAGGIORE --> >
MAGGIORE/UGUALE --> >=
MINORE --> <
MINORE/UGUALE --> <=
UGUALE-CONFRONTO --> == 
AND (entrambe vere) --> &&
OR (una delle due vere) --> || 
```
