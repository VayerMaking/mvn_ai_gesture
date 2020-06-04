from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)


RELAIS_1_GPIO = 17
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode


@app.route('/hello')
def hello():

    return "hello from the Raspberry Pi!"

@app.route('/on')
def on():

    return GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on

@app.route('/off')
def off():

     return GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out

app.run(host='0.0.0.0', port= 8090)

