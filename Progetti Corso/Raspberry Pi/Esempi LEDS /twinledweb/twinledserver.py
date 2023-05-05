import RPi.GPIO as GPIO
from flask import Flask, render_template

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
