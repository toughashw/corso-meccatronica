import RPi.GPIO as GPIO
import telepot
import time

# Configurazione dei GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configurazione dei pin dei LED
ledrosso = 14
ledgiallo = 18
ledverde = 7

GPIO.setup(ledrosso, GPIO.OUT)
GPIO.setup(ledgiallo, GPIO.OUT)
GPIO.setup(ledverde, GPIO.OUT)

# Funzioni per accendere e spegnere i LED
def accendi_led(pin):
    GPIO.output(pin, GPIO.HIGH)

def spegni_led(pin):
    GPIO.output(pin, GPIO.LOW)

def stato_led(pin):
    GPIO.input(pin)

# Funzione per gestire i messaggi del bot
def gestisci_messaggio(messaggio):
    chat_id = messaggio['chat']['id']
    testo = messaggio['text']

    if  testo == '/start':
        bot.sendMessage(chat_id, 'Benvenuto nel menu dei LED. \nScegli un'opzione: \n\nDigita 1. per accendere il LED Rosso\nDigita 2. Per spegnere il LED Rosso\nDigita 3. Per info sullo stato del LED Rosso\nDigita 4. Per accendere il LED Giallo \nDigita 5. Per spegnere il LED Giallo \nDigita 6. Per info sullo Stato del LED Giallo\nDigita 7. Per accendere il LED Verde \nDigita 8. Per spegnere il LED Verde \nDigita 9. Per info sullo Stato del LED Verde')

    elif testo == '1':
         accendi_led(led1)
         bot.sendMessage(chat_id, 'Il LED Rosso è acceso')

    elif testo == '2':
         spegni_led(led1)
         bot.sendMessage(chat_id, 'Il LED Rosso è spento')

    elif testo == '3':
         ledstate1 =  stato_led(led1)
         bot.sendMessage(chat_id,'Il LED Rosso è {}'.format(ledstate1))

    elif testo == '4':
         accendi_led(led2)
         bot.sendMessage(chat_id, 'Il LED Giallo è acceso')

    elif testo == '5':
         spegni_led(led2)
         bot.sendMessage(chat_id, 'Il LED Giallo è spento')

    elif testo == '6':
         ledstate2 = stato_led(led2)
         bot.sendMessage(chat_id, 'Il LED Giallo è {}'.format(ledstate2))

    elif testo == '7':
         accendi_led(led3)
         bot.sendMessage(chat_id, 'Il LED Verde è acceso')

    elif testo == '8':
         spegni_led(led3)
         bot.sendMessage(chat_id, 'Il LED Verde è spento')

    elif testo == '9':
         ledstate3 = stato_led(led3)
         bot.sendMessage(chat_id, 'Il LED Verde è {}'.format(ledstate3))
    else:
        bot.sendMessage(chat_id, 'Comando non valido')

# Configurazione del bot Telegram
bot = telepot.Bot('6041146609:AAEDVHZxIVlRE_uYHpUnK4du640WdKre3oo')
bot.message_loop(gestisci_messaggio)

# Loop infinito per mantenere il bot in ascolto dei messaggi
while True:
    time.sleep(10)

