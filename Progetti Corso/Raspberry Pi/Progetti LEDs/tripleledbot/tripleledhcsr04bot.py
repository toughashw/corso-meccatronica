import RPi.GPIO as GPIO
import telepot
import time
from time import sleep

# Inizializza il sensore HC-SR04
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Inizializza i pin dei LED
ledblue = 14
ledgiallo = 18
ledverde = 7
GPIO.setup(ledblue, GPIO.OUT)
GPIO.setup(ledgiallo, GPIO.OUT)
GPIO.setup(ledverde, GPIO.OUT)

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

def ledsonloop(distancecm):
    print('La distanza è: ',distancecm,'cm')

    if distancecm >0 and distancecm <=10:
       print('La distanza va male')
       print('Accendo LED Blue')
       GPIO.output(ledblue, True)
       GPIO.output(ledgiallo, False)
       GPIO.output(ledverde, False)

    elif distancecm >10 and distancecm <=20:
         print('La distanza va benino')
         print('Accendo LED Giallo')
         GPIO.output(ledrosso, False)
         GPIO.output(ledgiallo, True)
         GPIO.output(ledverde, False)

    elif distancecm >20 and distancecm <=30:
         print('La distanza va bene')
         print('Accendo LED Verde')
         GPIO.output(ledblue, False)
         GPIO.output(ledgiallo, False)
         GPIO.output(ledverde, True)

    else:
         GPIO.output(ledblue, False)
         GPIO.output(ledgiallo, False)
         GPIO.output(ledverde, False)

def ledsonchat(distancecm, chat_id):
    if distancecm >0 and distancecm <=10:
       bot.sendMessage(chat_id, 'La distanza va male')
       bot.sendMessage(chat_id, 'Accendo LED Blue')

    elif distancecm >10 and distancecm <=20:
         bot.sendMessage(chat_id, 'La distanza va benino')
         bot.sendMessage(chat_id, 'Accendo LED Giallo')

    elif distancecm >20 and distancecm <=30:
         bot.sendMessage(chat_id, 'La distanza va bene')
         bot.sendMessage(chat_id, 'Accendo LED Verde')

# Funzione per gestire i messaggi del bot
def gestisci_messaggio(messaggio):
    chat_id = messaggio['chat']['id']
    testo = messaggio['text']

    if testo == '/start':
       bot.sendMessage(chat_id, 'Benvenuto nel chatbot della distanza')

    elif testo == '/distanza':
         bot.sendMessage(chat_id, 'Distanza : {}cm'.format(distancecm))

# Configurazione del bot Telegram
bot = telepot.Bot('6041146609:AAEDVHZxIVlRE_uYHpUnK4du640WdKre3oo')
bot.message_loop(gestisci_messaggio)

while True:
   distancecm = misura_distanza()
   ledsonloop(distancecm)

   time.sleep(0.5)

GPIO.cleanup()