mport RPi.GPIO as GPIO
import telepot
import time

ledrosso = 14
ledgiallo = 18
ledverde = 7

GPIO.setmode(GPIO.BCM)

GPIO.setup(ledrosso, GPIO.OUT)
GPIO.setup(ledgiallo, GPIO.OUT)
GPIO.setup(ledverde, GPIO.OUT)

bot = telpot.Bot('6041146609:AAEDVHZxIVlRE_uYHpUnK4du640WdKre3oo')

def gestisci_messaggio(messaggio):
    chat_id = messaggio['chat']['id']
    testo = messaggio['text']
bot.message_loop(gestisci_messaggio)

def ledon(pin):
    GPIO.output(pin, GPIO.HIGH)

def ledoff(pin):
    GPIO.output(pin, GPIO.LOW)

def ledstate(pin):
    GPIO.input(pin)

if testo == '/start':
   bot.sendMessage(chat_id, '1: Accendi LED Rosso. \n2: 2:Spegni LED Rosso. \n3: Stato LED Rosso. \n4: Accendi LED Giallo. \n5: Spegni LED Giallo. \n6: Stato LED Giallo. \n7: Accendi LED Verde. \n8: Spegni LED Verde. \n9: Stato LED Verde. \n')

elif testo == '1':
     ledon(ledrosso)
     bot.sendMessage(chat_id, 'LED Rosso è Acceso')
elif testo == '2':
     ledoff(ledrosso)
     bot.sendMessage(chat_id, 'LED Rosso è Spento')
elif testo == '3':
     ledstate(ledrosso)
     statoR = ledstate(ledrosso)
match (statoR):
    case statoR'False':
    bot.sendMessage(chat_id, 'Il LED è spento')
    case statoR'True':
    bot.sendMessage(chat_id, 'Il LED è acceso')
elif testo == '4':
     ledon(ledgiallo)
     bot.sendMessage(chat_id, 'LED Giallo è Acceso')
elif testo == '5':
     ledoff(ledgiallo)
     bot.sendMessage(chat_id, 'LED Giallo è Spento')
elif testo == '6':
     ledstate(ledgiallo)
     statoG = ledstate(ledgiallo) 
match (statoG):
    case statoG'False':
    bot.sendMessage(chat_id, 'Il LED è spento')
    case statoG'True':
    bot.sendMessage(chat_id, 'Il LED è acceso')
elif testo =='7':
     ledon(ledverde)
     bot.sendMessage(chat_id, 'LED Verde è Acceso')
elif testo == '8':
     ledoff(ledverde)
     bot.sendMessage(chat_id, 'LED Verde è Spento')
elif testo =='9':
     ledstate(ledverde)
     statoV = ledstate(ledverde) 
match (statoV):
    case statoV'False':
    bot.sendMessage(chat_id, 'Il LED è spento')
    case statoV'True':
    bot.sendMessage(chat_id, 'Il LED è acceso')

while True:
    time.sleep(10)

