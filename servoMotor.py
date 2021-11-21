import RPi.GPIO as GPIO
import time

servo_pin = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

pwm = GPIO.PWM(servo_pin,50) # 50 Hz (20 ms PWM period)

pwm.start(7) # start PWM by rotating to 90 degrees

for i in range(0,3):
    pwm.ChangeDutyCycle(2.0) # rotate to 0 degrees
    time.sleep(0.5)
    pwm.ChangeDutyCycle(12.0) # rotate to 180 degrees
    time.sleep(0.5)
    pwm.ChangeDutyCycle(7.0) # rotate to 90 degrees
    time.sleep(0.5)

pwm.ChangeDutyCycle(0) # this prevents jitter
pwm.stop()
GPIO.cleanup()
