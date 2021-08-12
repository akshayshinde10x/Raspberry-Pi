import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
y = 12
GPIO.setup(8, GPIO.OUT) #red
GPIO.setup(10, GPIO.OUT) #green
GPIO.setup(y, GPIO.OUT) #yellow

while True:
	
	age = int(input("Please enter your Age : "))
	print(age)
	if age < 0:
		print("Enter a Positive Number")
		GPIO.output(y, GPIO.HIGH)
		highPin = y
	elif age >= 18 :
		print("You are eligible to Vote")
		GPIO.output(10, GPIO.HIGH)
		highPin = 10
	else:
		print("You can't Vote")
		GPIO.output(8, GPIO.HIGH)
		highPin = 8
		
	sleep(2)
	GPIO.output(highPin, GPIO.LOW)
	
