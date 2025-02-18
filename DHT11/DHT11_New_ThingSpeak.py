import thingspeak
import time
import adafruit_dht
from board import *

#GPIO 4
PIN = D4

channel_id = 10***85 # put here the ID of the channel you created before
write_key = 'ZLKA***3KPJ' # update the "WRITE KEY"

sensor = adafruit_dht.DHT11(PIN, use_pulseio=False)

def measure(channel):
    try:
        temperature = sensor.temperature
        humidity = sensor.humidity
        if humidity is not None and temperature is not None:
            print('Temperature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity))
        else:
            print('Did not receive any reading from sensor. Please check!')
        # update the value
        response = channel.update({'field1': temperature, 'field2': humidity})
    except:
           print("connection failure")

if __name__ == "__main__":
        channel = thingspeak.Channel(id=channel_id,api_key=write_key)
        while True:
            measure(channel)
        #free account has a limitation of 15sec between the updates
            time.sleep(15)
