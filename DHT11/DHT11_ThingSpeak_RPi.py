import thingspeak
import time
import Adafruit_DHT

channel_id = 10***85 # put here the ID of the channel you created before
write_key = 'ZLKA***3KPJ' # update the "WRITE KEY"

pin = 4
sensor = Adafruit_DHT.DHT11

def measure(channel):
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
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
