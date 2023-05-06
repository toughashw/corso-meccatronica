import RPi.GPIO as GPIO
import wiringpi
import telepot
import time

# Configurazione dei GPIO
wiringpi.wiringPiSetupGpio()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configurazione dei pin dei LED
led1 = 11
led2 = 13
wiringpi.pinMode(led1, wiringpi.OUTPUT)
wiringpi.pinMode(led2, wiringpi.OUTPUT)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

# Funzioni per accendere e spegnere i LED
def accendi_led(pin):
    GPIO.output(pin, GPIO.HIGH)
    wiringpi.digitalWrite(pin, wiringpi.HIGH)

def spegni_led(pin):
    GPIO.output(pin, GPIO.LOW)
    wiringpi.digitalWrite(pin, wiringpi.LOW)

def stato_led(pin):
    wiringpi.digitalRead(pin)

# Funzione per gestire i messaggi del bot
def gestisci_messaggio(messaggio):
    chat_id = messaggio['chat']['id']
    testo = messaggio['text']

    if testo == '/start':
        bot.sendMessage(chat_id, 'Benvenuto nel menu dei LED. Scegli un\'opzione: \n\n1. Accendi LED 1\n2. Spegni LED 1\n3. Stato LED 1\n4. Accendi LED 2 \n5. Spegni LED 2 \n6. Stato LED 2')

    elif testo == '1':
        accendi_led(led1)
        bot.sendMessage(chat_id, 'LED 1 è acceso')

    elif testo == '2':
        spegni_led(led1)
        bot.sendMessage(chat_id, 'LED 1 è spento')

    elif testo == '3':
         stato_led(led1)
    if   accendi_led(led1) == True):
         bot.sendMessage(chat_id, 'LED 1 è acceso')
    else:
        bot.sendMessage(chat_id, 'LED 1 è spento')

    elif testo == '4':
        accendi_led(led2)
        bot.sendMessage(chat_id, 'LED 2 è acceso')

    elif testo == '5':
        spegni_led(led2)
        bot.sendMessage(chat_id, 'LED 2 è spento')

    elif testo == '6':
        stato_led(led2)
    if  accendi_led(led2) == True
         bot.sendMessage(chat_id, 'LED 2 è acceso')
    else:
        bot.sendMessage(chat_id, 'LED 2 è spento')

    else:
        bot.sendMessage(chat_id, 'Comando non valido')

# Configurazione del bot Telegram
bot = telepot.Bot('INSERISCI_QUI_IL_TOKEN_DEL_TUO_BOT')
bot.message_loop(gestisci_messaggio)

# Loop infinito per mantenere il bot in ascolto dei messaggi
while True:
    time.sleep(10)
