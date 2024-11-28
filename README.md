### **README.md**

# ICM42688P CircuitPython Driver

This repository contains a CircuitPython driver for the **ICM42688P**, a high-performance 6-axis motion tracking sensor. This driver is a **port from the original C implementation** used in embedded systems to a Python implementation specifically designed for CircuitPython on microcontrollers such as the RP2040.

## Features
- **Accelerometer Support:** Reads X, Y, Z acceleration in G (gravitational force).
- **Gyroscope Support:** Reads X, Y, Z angular velocity in degrees per second (DPS).
- **Temperature Sensor:** Reads the internal temperature of the sensor in Celsius.
- **SPI Communication:** Communicates with the sensor over SPI using CircuitPython's `busio`.

## Requirements
- CircuitPython-compatible microcontroller (e.g., Raspberry Pi Pico with RP2040).
- CircuitPython installed on your microcontroller.
- The following CircuitPython libraries:
  - `busio` (for SPI communication)
  - `digitalio` (for handling GPIO pins like CS)
  - `board` (for accessing pin definitions)

## Installation
1. **Copy the Driver**  
   Download the `icm42688p.py` file and save it to the `lib` directory on your CircuitPython device.

2. **Install CircuitPython Libraries**  
   Make sure you have the `busio`, `digitalio`, and `board` libraries available. These are typically included in the CircuitPython firmware.

3. **Wiring the Sensor**  
   Connect the ICM42688P sensor to your microcontroller as follows:
   ```
   Sensor Pin      Microcontroller Pin
   -----------     -------------------
   SCK             GP2 (SPI Clock)
   MOSI            GP3 (SPI Master Out Slave In)
   MISO            GP4 (SPI Master In Slave Out)
   CS              GP5 (Chip Select)
   GND             GND
   VCC             3.3V
   ```

## Usage
### Example Code
```python
from icm42688p import ICM42688P
import board
import busio
import digitalio
import time

# Initialize SPI bus
spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)

# Initialize Chip Select (CS) pin
cs = board.GP5

# Create an instance of the ICM42688P driver
imu = ICM42688P(spi, cs)

# Initialize the sensor
imu.initialize()

# Read sensor data in a loop
while True:
    accel = imu.read_accelerometer()
    gyro = imu.read_gyroscope()
    temp = imu.read_temperature()

    print(f"Accelerometer: {accel}")  # Acceleration in G
    print(f"Gyroscope: {gyro}")  # Angular velocity in DPS
    print(f"Temperature: {temp:.2f}°C")  # Temperature in Celsius
    time.sleep(1)
```

## API Reference

### `ICM42688P(spi, cs_pin)`
- **Description:** Initializes the ICM42688P driver with the SPI bus and Chip Select (CS) pin.
- **Parameters:**
  - `spi`: A `busio.SPI` instance for SPI communication.
  - `cs_pin`: The GPIO pin used for Chip Select (CS).

### `initialize()`
- **Description:** Configures and initializes the ICM42688P sensor. Performs a soft reset, verifies the device, and configures the accelerometer and gyroscope.

### `read_accelerometer()`
- **Description:** Reads raw accelerometer data and converts it to G units.
- **Returns:** A tuple `(accel_x, accel_y, accel_z)` in G.

### `read_gyroscope()`
- **Description:** Reads raw gyroscope data and converts it to DPS.
- **Returns:** A tuple `(gyro_x, gyro_y, gyro_z)` in degrees per second.

### `read_temperature()`
- **Description:** Reads the internal temperature of the sensor and converts it to Celsius.
- **Returns:** The temperature in Celsius as a float.

## Porting Notes
This Python implementation is a **direct port** of the original C driver used in embedded systems:
- SPI communication is managed using CircuitPython's `busio` library.
- The locking mechanisms (`_spi_lock` and `_spi_unlock`) are adapted to CircuitPython's `try_lock` and `unlock` methods.
- All registers and configuration constants are preserved from the original C implementation.

## Limitations
- This driver only supports **SPI communication**. I2C is not currently implemented.
- Ensure your CircuitPython device has sufficient memory to handle the driver and its dependencies.

## Contributing
Contributions are welcome! If you find bugs or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License
This driver is provided under the MIT License. See the `LICENSE` file for details.

---

This README provides all the necessary details for understanding, using, and extending the driver. Let me know if you'd like further adjustments!
