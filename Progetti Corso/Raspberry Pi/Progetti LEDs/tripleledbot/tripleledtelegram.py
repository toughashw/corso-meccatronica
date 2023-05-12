import RPi.GPIO as GPIO
import telepot
import time
from time import sleep

ledrosso = 14
ledgiallo = 18
ledverde = 7

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ledrosso, GPIO.OUT)
GPIO.setup(ledgiallo, GPIO.OUT)
GPIO.setup(ledverde, GPIO.OUT)

def ledon(pin):
    GPIO.output(pin, GPIO.HIGH)

def ledoff(pin):
    GPIO.output(pin, GPIO.LOW)

def ledstate(pin, chat_id):
    if GPIO.input(pin) == True:
       bot.sendMessage(chat_id, 'il LED è acceso')
    elif GPIO.input(pin) == False:
       bot.sendMessage(chat_id, 'il LED è spento')

def gestisci_messaggio(messaggio):
    chat_id = messaggio['chat']['id']
    testo = messaggio['text']

    if testo == '/start':
       bot.sendMessage (chat_id, '1. Accendi LED Rosso. \n2. Spegni LED Rosso. \n3. Stato LED Rosso. \n4. Accendi LED Giallo. \n5. Spegni LED Giallo. \n6. Stato LED Giallo. \n7. Accendi LED Verde. \n8. Spegni LED Verde. \n9. Stato LED Verde.')
    elif testo == '1':
         ledon(ledrosso)
         bot.sendMessage (chat_id, 'LED Rosso è Acceso')
    elif testo == '2' :
         ledoff(ledrosso)
         bot.sendMessage(chat_id, 'LED Rosso è Spento')
    elif testo == '3':
         ledstate(ledrosso, chat_id)
    elif testo == '4':
         ledon(ledgiallo)
         bot.sendMessage (chat_id, 'LED Giallo è Acceso')
    elif testo == '5':
         ledoff(ledgiallo)
         bot.sendMessage(chat_id, 'LED Giallo è Spento')
    elif testo == '6':
         ledstate(ledgiallo, chat_id)
    elif testo == '7':
         ledon (ledverde)
         bot.sendMessage (chat_id, 'LED Verde è Acceso')
    elif testo == '8':
         ledoff(ledverde)
         bot.sendMessage(chat_id, 'LED Verde è Spento')
    elif testo == '9':
         ledstate(ledverde, chat_id)

bot = telepot.Bot('6041146609:AAEDVHZxIVlRE_uYHpUnK4du640WdKre3oo')
bot.message_loop(gestisci_messaggio)

while True:
    time.sleep(10)

