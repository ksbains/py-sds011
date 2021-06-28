from sds011 import *
sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
from datetime import *
import time
import board
import adafruit_dht
import schedule
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
from api import *
data = []
username = "killah-bee"
temp = 9999
humidity = 9999

def recordDHT():
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        global temp
        temp = temperature_f
        global humidity
        humidity = dhtDevice.humidity
        # print("the temp is ", temp)
        # print("the humid is ", humidity)
    
    except RuntimeError as error:
    #     # Errors happen fairly often, DHT's are hard to read, just keep going
        # print(error.args[0])
        time.sleep(1)
    
def recordData():
    ct = datetime.now()
    pmt_2_5, pmt_10 = sensor.query()
    print(username,str(pmt_2_5),str(pmt_10), temp, humidity, str(ct))
    addSensor(username, str(pmt_2_5),str(pmt_10), temp, humidity, str(ct))

# every 10 seconds record data to dict
schedule.every(30).seconds.do(recordData)
# every 2 seconds record temp and humid data'=
schedule.every(2).seconds.do(recordDHT)

while 1:
    schedule.run_pending()
    time.sleep(1)

