from sds011 import *
sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
from datetime import *
import time
import schedule
from api import *
data = []
username = "killah-bee"


def recordData():
    ct = datetime.now()
    pmt_2_5, pmt_10 = sensor.query()
    temp = "invalid"
    humidity = "invalid"
    print(username,str(pmt_2_5),str(pmt_10), temp, humidity, str(ct))
    addSensor(username, str(pmt_2_5),str(pmt_10), temp, humidity, str(ct))

# every 10 seconds record data to dict
schedule.every(30).seconds.do(recordData)
# every minute create and fill file with data. 
# schedule.every(24).hours.do(recordData)

while 1:
    schedule.run_pending()
    time.sleep(1)

