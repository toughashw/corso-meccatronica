import RPi.GPIO as GPIO
from flask import Flask, render_template

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/on/<int:led>')
def led_on(led):
    GPIO.output(led, GPIO.HIGH)
    return 'LED ' + str(led) + ' Acceso'

@app.route('/led/off/<int:led>')
def led_off(led):
    GPIO.output(led, GPIO.LOW)
    return 'LED ' + str(led) + ' Spento'

@app.route('/led/state/<int:led>')
def led_state(led):
    GPIO.input(led)
    if GPIO.input(led) == HIGH:
    return 'LED ' + str(led) + ' Acceso'
    else:
    return 'LED ' + str(led) + ' Spento'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
