import time
import RPi.GPIO as GPIO
from keypad import keypad
 
GPIO.setwarnings(False)
# Initialize
kp = keypad(columnCount = 3) 

while True:
        
    print("Please press * key and then enter password")
    # waiting for a keypress
    digit = None
    while digit == None:
        digit = kp.getKey()
    
    print (digit)
    time.sleep(0.5)
 
    if(digit == '*'):
        print("Enter your 4 Digit password and then press #")
        seq = []
        for i in range(5):
            digit = None
            while digit == None:
                digit = kp.getKey()
                
            print (digit)
            seq.append(digit)
            time.sleep(0.4)
     
        print(seq)
        if seq == [1, 2, 3, 4, '#']:
		print ("Code accepted")
        else:
		print("Please try again !")
    else:
        print("Wrong key is Pressed")

