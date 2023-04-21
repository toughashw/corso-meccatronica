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
const int nomepint = numeropin;
#define nomepin numeroPin;
```

- DICHIARIAZIONE INGRESSI/USCITE
```
void setup() {
pinMode(nomepin/numeropin,HIGH/LOW);
}
```

- LETTURA/SCRITTURA DA INGRESSI ANALOGICI/DIGITALI
```
void loop() {
digitalRead(nomepin/numeropin);
digitalWrite(nomepin/numeropin, HIGH/LOW);
analogRead(nomepin/numeropin);
analogWrite()
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
