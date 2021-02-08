from sds011 import *
sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
import datetime
import csv

with open('pmtData','w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(["time", "pmt 2.5", "pmt 10"])

    for i in range(1, 10):
        ct = datetime.datetime.now()
        pmt_2_5, pmt_10 = sensor.query()
        thewriter.writerow([str(ct), str(pmt_2_5), str(pmt_10)])




# print("The pmt values are:")
# print("PMT 2.5: " + str(pmt_2_5))
# print("PMT 10: " + str(pmt_10))

