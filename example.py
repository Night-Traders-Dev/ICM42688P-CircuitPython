from icm42688p import ICM42688P  # Custom driver for the ICM42688P sensor
import board
import digitalio
import busio
import time

# Initialize the SPI bus
# The SPI bus requires specifying the clock (SCK), Master Out Slave In (MOSI), and Master In Slave Out (MISO) pins
spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)

# Define the Chip Select (CS) pin
# The CS pin is used to select the ICM42688P device during SPI communication
cs = board.GP5

# Create an instance of the ICM42688P class
# Pass the SPI bus and CS pin to the driver
imu = ICM42688P(spi, cs)

# Initialize the sensor
# This step performs a soft reset and configures the accelerometer and gyroscope
imu.initialize()

# Start reading sensor data in an infinite loop
while True:
    # Read accelerometer data in G (gravitational force)
    accel = imu.read_accelerometer()

    # Read gyroscope data in degrees per second (DPS)
    gyro = imu.read_gyroscope()

    # Print the accelerometer and gyroscope data to the console
    print(f"Accelerometer: {accel}")  # Example output: Accelerometer: (0.01, -0.02, 9.81)
    print(f"Gyroscope: {gyro}")  # Example output: Gyroscope: (0.1, -0.2, 0.0)

    # Wait for 1 second before reading data again
    time.sleep(1)

