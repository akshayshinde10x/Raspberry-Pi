#pip3 install adafruit-io

import time
import RPi.GPIO as GPIO
from Adafruit_IO import Client

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

ADAFRUIT_IO_USERNAME = "aks*****ine"
ADAFRUIT_IO_KEY = "aio_sTDz******1vqPIR"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
distance_feed = aio.feeds('light')

while True:
	print("Receiving data..")
	status = aio.receive(distance_feed.key).value
	print(status)
	if status == "ON":
		GPIO.output(2,True)
        print("LED ON")
	else:
		GPIO.output(2,False)
        print("LED OFF")
	time.sleep(5)