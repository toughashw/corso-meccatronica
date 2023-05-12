import RPi.GPIO
import telepot
import time
from time import sleep

sensor = 1
pin_relay = [14, 15, 18, 23, 24, 25, 8, 7]

GPIO.setmode(GPIO.BCM)

GPIO.setup(sensore, GPIO.IN)

for pin in pin_relay:
    GPIO.setup(pin_relay[i], GPIO.OUT)

def relayon(pin_relay):
    GPIO.output(pin_relay[i], GPIO.HIGH)

def relayoff(pin_relay):
    GPIO.output(pin_relay[i], GPIO.LOW)

def relaystate(pin_relay, chat_id):
    if GPIO.input(pin) == True:
       bot.sendMessage(chat_id, 'Il Relay è acceso')
    elif GPIO.input(pin) == False:
       bot.sendMessage(chat_id, 'Il Relay è spento')

def gestisci_messaggio(messaggio):
    chat_id = messaggio['chat']['id']
    testo = messaggio['text']
    if testo == '/start':
       bot.sendMessage (chat_id, '1. Accendi i primi 4 Relay. \n2. Accendi i secondi 4 Relay. \n3. Accendi i secondi 4 Relay. \n4. Spegni i secondi 4 Relay')
    elif testo == '1':
         for i in range(4):
         relayon(pin)
         bot.sendMessage (chat_id, ' Il primo gruppo è accesso')
    elif testo == '2' :
         for i in range(4):
         relayoff(pin)
         bot.sendMessage(chat_id, 'Il primo gruppo è spento')
    elif testo == '3' :
         for i in range(4,8):
         relayon(pin)
         bot.sendMessage(chat_id, 'Il secondo gruppo è acceso')
    elif testo == '4' :
         for i in range(4,8):
         relayoff(pin)
         bot.sendMessage(chat_id, 'Il secondo gruppo è spento')

bot = telepot.Bot('6041146609:AAEDVHZxIVlRE_uYHpUnK4du640WdKre3oo')
bot.message_loop(gestisci_messaggio)

while True:
    time.sleep(10)
