import RPi.GPIO as GPIO  # Import GPIO library
import time  # Import time library


def detectPosition(trig: int, echo: int) -> float:
    GPIO.output(trig, False)  # Set TRIG as LOW
    time.sleep(2)  # Delay of 2 seconds

    GPIO.output(trig, True)  # Set TRIG as HIGH
    time.sleep(0.00001)  # Delay of 0.00001 seconds
    GPIO.output(trig, False)  # Set TRIG as LOW

    # pulse initialization
    pulse_start = 0
    pulse_end = 0

    if GPIO.input(echo) == 0:
        pulse_start = time.time()  # Time of the last  LOW pulse
    else:
        pulse_end = time.time()  # Time of the last HIGH pulse

    pulse_duration = pulse_end - pulse_start  # pulse duration to a variable
    distance = pulse_duration * 17150  # Calculate distance

    return round(distance, 2)
