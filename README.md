# Corso di Meccatronica
Repository del Corso di Meccatronica della Regione Puglia

- LIBRERIE
```
#include <nomelibreria.h>
```

- DICHIARIAZIONE PINS
```
const int nome-in-out = numeropin;
#define nome IN/OUT NumeroPin;
```

- LETTURA/SCRITTURA DA INGRESSI ANALOGICI/DIGITALI
```
digitalRead(nomepin/numeropin)
digitalWrite(nomepin/numeropin, HIGH/LOW)
analogRead(nomepin/numeropin)
analogWrite()
```

- OPERAZIONI CON SERIALE
void setup() {
Serial.begin(9600); --> Legge da Seriale con baund a 9600
}
void loop() {
Serial.print("TESTO"); --> Stampa su monitor seriale una stringa di testo
Serial.print(dati);    --> Stampa su monitor seriale lo stream di dati
Serial.println("TESTO"); --> Stampa a capo su monitor seriale una stringa di testo
Serial.println(dati);  --> Stampa a capo su monitor seriale lo stream di dati
}
