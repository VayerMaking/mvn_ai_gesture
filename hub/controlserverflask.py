from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)


relaypin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)


@app.route('/hello')
def hello():

    return "hello from the Raspberry Pi!"

@app.route('/on')
def on():

    return GPIO.output(relaypin, GPIO.HIGH)

@app.route('/off')
def off():

     return GPIO.output(relaypin, GPIO.LOW) 

app.run(host='0.0.0.0', port= 8090)
