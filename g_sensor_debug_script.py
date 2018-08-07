import time
from gravsensor.adxl345 import adxl345

accel = adxl345()

while True:
  accel.get_Gxyz()
  print "x:" , accel.x
  print "y:" , accel.y
  print "z:" , accel.z
  print ""
  time.sleep(1)
