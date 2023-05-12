import RPi.GPIO as GPIO
import telepot
import time
from time import sleep

pin_relay = [14, 15, 18, 23, 24, 25, 8, 7]

GPIO.setmode(GPIO.BCM)

for pin in pin_relay:
    GPIO.setup(pin_relay[i], GPIO.OUT)

def relayfirston(pin):
  for i in range(4):
      GPIO.output(pin_relay[i], GPIO.HIGH)

def relayfirstoff(pin):
  for i in range(4):
    GPIO.output(pin_relay[i], GPIO.LOW)

def relaysecondon(pin):
  for i in range(4,8):
      GPIO.output(pin_relay[i], GPIO.HIGH)

def relaysecondoff(pin):
  for i in range(4,8):
    GPIO.output(pin_relay[i], GPIO.LOW)

def relaystate(pin, chat_id):
  for pin in pin_relay:
    if GPIO.input(pin) == True:
       bot.sendMessage(chat_id, 'Il Relay è acceso')
    elif GPIO.input(pin) == False:
       bot.sendMessage(chat_id, 'Il Relay è spento')

def gestisci_messaggio(messaggio):
    chat_id = messaggio['chat']['id']
    testo = messaggio['text']
    if testo == '/start':
       bot.sendMessage (chat_id, '1. Accendi i primi 4 Relay. \n2. Spegni i primi 4 Relay. \n3. Accendi i secondi 4 Relay. \n4. Spegni i secondi 4 Relay')
    elif testo == '1':
         bot.sendMessage (chat_id, ' Il primo gruppo è accesso')
         for i in range(4):
         relayfirston(pin)
    elif testo == '2' :
         bot.sendMessage(chat_id, 'Il primo gruppo è spento')
         for i in range(4):
         relayfirstoff(pin)
    elif testo == '3' :
         bot.sendMessage(chat_id, 'Il secondo gruppo è acceso')
         for i in range(4,8):
         relaysecondon(pin)
    elif testo == '4' :
         bot.sendMessage(chat_id, 'Il secondo gruppo è spento')
         for i in range(4,8):
         relaysecondoff(pin)

bot = telepot.Bot('6041146609:AAEDVHZxIVlRE_uYHpUnK4du640WdKre3oo')
bot.message_loop(gestisci_messaggio)

while True:
    time.sleep(10)
