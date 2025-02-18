#pip3 install adafruit-circuitpython-dht

import adafruit_dht
from board import *

#GPIO 4
PIN = D4

sensor = adafruit_dht.DHT11(PIN, use_pulseio=False)

temperature = sensor.temperature
humidity = sensor.humidity

print(f"Temperature={temperature:.2f} °C")
print(f"Humidity={humidity:.2f} %")
