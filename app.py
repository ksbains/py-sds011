from sds011 import *
sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
import datetime
import time
import schedule
import csv

def record():
    ct = datetime.datetime.now()
    pmt_2_5, pmt_10 = sensor.query()
    print(str(ct), str(pmt_2_5), str(pmt_10))
    with open('pmtData','w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow([str(ct), str(pmt_2_5), str(pmt_10)])


with open('pmtData','w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(["time", "pmt 2.5", "pmt 10"])
    

schedule.every(30).seconds.do(record)


while 1:
    schedule.run_pending()
    time.sleep(1)



# print("The pmt values are:")
# print("PMT 2.5: " + str(pmt_2_5))
# print("PMT 10: " + str(pmt_10))

