from sds011 import *
sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)

pmt_2_5, pmt_10 = sensor.query()

print("The pmt values are:")
print("PMT 2.5: " + str(pmt_2_5))
print("PMT 10: " + str(pmt_10))

