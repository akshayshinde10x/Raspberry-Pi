import time
import Adafruit_DHT
from Adafruit_IO import Client, Feed

DHT_DATA_PIN = 4

ADAFRUIT_IO_USERNAME = "aks****e"
ADAFRUIT_IO_KEY = "aio_s********vqPIR"

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

temperature_feed = aio.feeds('temp')
humidity_feed = aio.feeds('humidity')

dht22_sensor = Adafruit_DHT.DHT11

while True:
    
    try:
        humidity, temperature = Adafruit_DHT.read_retry(dht22_sensor, DHT_DATA_PIN)
        
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
            
            temperature = '%.2f'%(temperature)
            humidity = '%.2f'%(humidity)
            aio.send(temperature_feed.key, str(temperature))
            aio.send(humidity_feed.key, str(humidity))
        else:
            print('Failed to get DHT22 Reading, trying again in ', DHT_READ_TIMEOUT, 'seconds')
        
        time.sleep(5)
    except:
        print("Exception occured..")
