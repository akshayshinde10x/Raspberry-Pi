from Adafruit_IO import Client
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)  
pwm = GPIO.PWM(12, 100) 

ADAFRUIT_IO_USERNAME = "abc"
ADAFRUIT_IO_KEY = "aio_uz***PUX"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

slider_feed = aio.feeds('slider')
status=0                               
pwm.start(status)                   

while True:
	status = aio.receive(slider_feed.key).value
	print(status)
	pwm.ChangeDutyCycle(int(status))
	time.sleep(0.001)
pwm.stop()                        
GPIO.cleanup()
