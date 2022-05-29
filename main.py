import RPi.GPIO as GPIO
from LakeContour import detectPosition, get_lat_long
from LakeContour.utils import connect, parseData, open_browser, query_link

# GPIO pin number
TRIG = 24  # Associate pin 15 to TRIG
ECHO = 23  # Associate pin 14 to Echo

# Aduino setup
port = "/dev/ttyS0"

# GPGGA Info for GPS sensor
GPGGA_info = "$GPGGA,"


def setup():
    GPIO.setmode(GPIO.BCM)  # Set GPIO pin numbering

    GPIO.setup(TRIG, GPIO.OUT)  # Set pin as GPIO out
    GPIO.setup(ECHO, GPIO.IN)  # Set pin as GPIO in

    # Connect arduino serial
    arduino = connect(port)

    return arduino


if __name__ == '__main__':
    serial_connect = setup()
    while True:
        try:
            # get lake depth data from sensor
            lake_depth = detectPosition(TRIG, ECHO)

            # get buffer gps sensor data
            gps_sensor_data = parseData(serial_connect, gpgga_info=GPGGA_info)

            # parse NMEA time, longitude and latitude from buffer data
            nmea_time, latitude, longitude = get_lat_long(gps_sensor_data)

            # query link to search position on Google Maps API
            formatted_gmaps_link = query_link(latitude, longitude)

            print(f"Kedalaman Danau: {lake_depth} | Latitude: {latitude} | Longitude: {longitude}")

        except KeyboardInterrupt:
            open_browser(formatted_gmaps_link)

