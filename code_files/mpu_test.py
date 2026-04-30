import smbus
import time

# MPU6050 I2C address
MPU_ADDR = 0x68

# Power management register
PWR_MGMT_1 = 0x6B

# Register addresses
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H  = 0x43

bus = smbus.SMBus(1)

# Wake up MPU6050
bus.write_byte_data(MPU_ADDR, PWR_MGMT_1, 0)

def read_raw_data(addr):
    high = bus.read_byte_data(MPU_ADDR, addr)
    low = bus.read_byte_data(MPU_ADDR, addr + 1)
    
    value = (high << 8) | low
    
    if value > 32768:
        value = value - 65536
    return value

while True:
    # Accelerometer
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_XOUT_H + 2)
    acc_z = read_raw_data(ACCEL_XOUT_H + 4)

    # Gyroscope
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_XOUT_H + 2)
    gyro_z = read_raw_data(GYRO_XOUT_H + 4)

    print("Accel X:", acc_x, "Y:", acc_y, "Z:", acc_z,
          " | Gyro X:", gyro_x, "Y:", gyro_y, "Z:", gyro_z)

    time.sleep(0.5)