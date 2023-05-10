import RPi.GPIO as GPIO
import time
import telepot

# Inizializza il sensore HC-SR04
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Inizializza i pin dei LED
ledrosso = 14
ledgiallo = 18
ledverde = 7
GPIO.setup(ledrosso, GPIO.OUT)
GPIO.setup(ledgiallo, GPIO.OUT)
GPIO.setup(ledverde, GPIO.OUT)

# Funzione per gestire i messaggi del bot
def gestisci_messaggio(messaggio):
    chat_id = messaggio['chat']['id']
    testo = messaggio['text']

def misura_distanza():
    # Invia un impulso al sensore
    GPIO.output(TRIG, False)
    time.sleep(0.5)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Attendi la risposta del sensore
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calcola la durata dell'impulso
    pulse_duration = pulse_end - pulse_start

    # Calcola la distanza in cm
    distance = pulse_duration * 17150
    distancecm = round(distance, 2)
    return distancecm
    print('La distanza è:',distancecm,'cm')

while True:
    # Accendi il LED corrispondente alla distanza
    distancecm = misura_distanza()
    if distancecm  >0 and distancecm <=10:
    GPIO.output(ledrosso, True)
    GPIO.output(ledgiallo, False)
    GPIO.output(ledverde, False)
    bot.sendMessage(chat_id, 'Distanza')
    elif distancecm >10 and distancecm <=20:
    GPIO.output(ledrosso, False)
    GPIO.output(ledgiallo, True)
    GPIO.output(ledverde, False)
    bot.sendMessage(chat_id, 'Distanza')
    elif distancecm >20 and distancecm <=30:
    GPIO.output(ledrosso, False)
    GPIO.output(ledgiallo, False)
    GPIO.output(ledverde, True)
    bot.sendMessage(chat_id, 'Distanza')
    else:
    GPIO.output(ledrosso, False)
    GPIO.output(ledgiallo, False)
    GPIO.output(ledverde, False)

# Configurazione del bot Telegram
bot = telepot.Bot('6041146609:AAEDVHZxIVlRE_uYHpUnK4du640WdKre3oo')
bot.message_loop(gestisci_messaggio)

# Loop infinito per mantenere il bot in ascolto dei messaggi
while True:
    time.sleep(10)