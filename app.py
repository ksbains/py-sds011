from sds011 import *
sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
from datetime import *
import time
import schedule
import csv


today = date.today()
fileName = today.strftime("%m.%d.%y")
fileName = fileName +".csv"
data = []


def recordData():
    f = open(fileName,'a', newline='')
    fieldNames = ["time", "pmt 2.5", "pmt 10"]
    thewriter = csv.DictWriter(f, fieldnames=fieldNames)
    thewriter.writeheader()
    for i in data:
        thewriter.writerow(i)


def record():
    ct = datetime.now()
    pmt_2_5, pmt_10 = sensor.query()
    print(str(ct), str(pmt_2_5), str(pmt_10))
    data.append({"time": str(ct), 'pmt 2.5': str(pmt_2_5), 'pmt 10': str(pmt_10)})

# every 10 seconds record data to dict
schedule.every(1).seconds.do(record)
#every minute create and fill file with data. 
schedule.every(10).seconds.do(recordData)



while 1:
    schedule.run_pending()
    time.sleep(1)

