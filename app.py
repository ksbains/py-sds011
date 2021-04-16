from sds011 import *
sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
from datetime import *
import time
import schedule
import csv
data = []
def recordData():
    today = date.today()
    fileName = today.strftime("%m.%d.%y")
    fileName = fileName +".csv"
    with open(fileName,'a', newline='') as fileObject:
        fieldNames = ["time", "pmt 2.5", "pmt 10"]
        writer = csv.DictWriter(fileObject, fieldnames=fieldNames)
        writer.writeheader()
        for i in data:
            writer.writerow(i)
    data = []

def record():
    ct = datetime.now()
    pmt_2_5, pmt_10 = sensor.query()
    print(str(ct), str(pmt_2_5), str(pmt_10))
    data.append({"time": str(ct), 'pmt 2.5': str(pmt_2_5), 'pmt 10': str(pmt_10)})

# every 10 seconds record data to dict
schedule.every(30).seconds.do(record)
#every minute create and fill file with data. 
schedule.every(24).hours.do(recordData)



while 1:
    schedule.run_pending()
    time.sleep(1)

