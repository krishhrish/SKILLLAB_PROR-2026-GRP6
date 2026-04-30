OLED - MPU code
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont
from mpu6050 import mpu6050
import time
import math

# -------- CONFIG --------
OLED_ADDR = 0x3C
MPU_ADDR  = 0x68
# -----------------------

# OLED setup
serial = i2c(port=1, address=OLED_ADDR)
device = sh1106(serial)

# MPU setup
sensor = mpu6050(MPU_ADDR)

font = ImageFont.load_default()

try:
    while True:
        # Read acceleration
        accel = sensor.get_accel_data()

        ax = accel['x']
        ay = accel['y']
        az = accel['z']

        # Calculate magnitude
        total_acc = math.sqrt(ax**2 + ay**2 + az**2)

        # Create display image
        width = device.width
        height = device.height
        image = Image.new("1", (width, height))
        draw = ImageDraw.Draw(image)

        # Display text
        draw.text((0, 0),  "MPU6050 Accel", font=font, fill=255)
        draw.text((0, 12), f"Ax: {ax:.2f}", font=font, fill=255)
        draw.text((0, 24), f"Ay: {ay:.2f}", font=font, fill=255)
        draw.text((0, 36), f"Az: {az:.2f}", font=font, fill=255)
        draw.text((0, 50), f"A: {total_acc:.2f} g", font=font, fill=255)

        # Show on OLED
        device.display(image)

        time.sleep(0.2)

except KeyboardInterrupt:
    device.clear()