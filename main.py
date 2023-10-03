import time

from stepperdriver import TMC2209
from communication import Serial
from util import Pins
from uvsensor import VEML6075


# Decorator for logging
def log_data(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time} seconds")
        return result

    return wrapper


if __name__ == '__main__':
    # Constants for calibration and tracking
    TARGET_UV_THRESHOLD = 1000  # Adjust this threshold based on your calibration
    HORIZONTAL_SPEED = 0.5  # Adjust the speed as needed
    VERTICAL_SPEED = 0.3  # Adjust the speed as needed

    tx_steppers = Pins.A1
    rx_steppers = Pins.A2

    soft_serial = Serial(tx_steppers, rx_steppers)

    # Initialize UV sensors
    uv_sensors = [VEML6075(1, soft_serial),
                  VEML6075(2, soft_serial),
                  VEML6075(3, soft_serial),
                  VEML6075(4, soft_serial)]

    # Initialize motors
    horizontal_motor = TMC2209(1, soft_serial)
    vertical_motor = TMC2209(2, soft_serial)


    # Function to track the sun
    @log_data
    def track_sun():
        while True:
            # hieronder wat voorbeeld logica
            uv_values = [sensor.read_uv() for sensor in uv_sensors]
            # avg_uv_value = sum(uv_values) / len(uv_values)

            # Check if the average UV value is above the threshold
            # if avg_uv_value > TARGET_UV_THRESHOLD:
            if True:
                # Calculate adjustments for horizontal and vertical motors
                horizontal_adjustment = 0  # Calculate based on sensor data
                vertical_adjustment = 0  # Calculate based on sensor data

                # Move the motors to adjust the solar panel position
                horizontal_motor.move(HORIZONTAL_SPEED * horizontal_adjustment)
                vertical_motor.move(VERTICAL_SPEED * vertical_adjustment)
                # Move the motors to adjust the solar panel position
                horizontal_motor.move(HORIZONTAL_SPEED * horizontal_adjustment)
                vertical_motor.move(VERTICAL_SPEED * vertical_adjustment)
            time.sleep(1)  # Adjust the sleep duration as needed

    if __name__ == "__main__":
        track_sun()
