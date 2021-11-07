import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)  
pwm = GPIO.PWM(12, 100) 
                           
pwm.start(0)                   

while True:

	for i in range(1,100):
		pwm.ChangeDutyCycle(int(i))
		time.sleep(0.01)
	
pwm.stop()                        
GPIO.cleanup()
