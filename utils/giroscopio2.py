import time
from mpu6050 import mpu6050

sensor = mpu6050(0x68)

while True:
    dato = sensor.get_accel_data()
    print dato
    time.sleep(1)
