#pip3 install picamera

from picamera import PiCamera
import time

camera = PiCamera()
time.sleep(2)

camera.capture("/home/pi/Pictures/img.jpg")
print("Done.")
