from digitalio import DigitalInOut, Direction
from icm42688p import ICM42688P

import board
import busio
import digitalio
import microcontroller
import time

spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)
cs = board.GP5

imu = ICM42688P(spi, cs)
imu.initialize()

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT


def display_console():
    print(f"Accelerometer: {accel}")
    print(f"Gyroscope: {gyro}")
    print(f"Temperature: {temp:.2f}°C")
    print(f"Temp0/1: {cpu_temp0:.2f}/{cpu_temp1:.2f} °C")



while True:
    led.value = True
    accel = imu.read_accelerometer()
    gyro = imu.read_gyroscope()
    temp = imu.read_temperature()
    cpu_temp0 = microcontroller.cpus[0].temperature
    cpu_temp1 = microcontroller.cpus[1].temperature
    display_console()
    time.sleep(1)
