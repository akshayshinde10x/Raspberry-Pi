import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT) #GPIO 2 -> Red LED as output
GPIO.setup(14,GPIO.IN) #GPIO 14 -> IR sensor as input

while 1:
    if(GPIO.input(14)==True): #object is far away
        GPIO.output(2,True) #Red led ON
        print("LED ON")
        time.sleep(1)
    
    if(GPIO.input(14)==False): #object is near
        GPIO.output(2,False) # Red led OFF
        print("LED OFF")
        time.sleep(1)
