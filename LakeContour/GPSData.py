from .utils import convert_to_degrees


def get_lat_long(nmea_buffer: list) -> tuple:
    nmea_time = nmea_buffer[0]  # extract time from GPGGA string
    nmea_latitude = nmea_buffer[1]  # extract latitude from GPGGA string
    nmea_longitude = nmea_buffer[3]  # extract longitude from GPGGA string

    lat = float(nmea_latitude)  # convert string into float for calculation
    long = float(nmea_longitude)  # convertr string into float for calculation

    lat_in_degrees = convert_to_degrees(lat)  # get latitude in degree decimal format
    long_in_degrees = convert_to_degrees(long)  # get longitude in degree decimal format

    return nmea_time, lat_in_degrees, long_in_degrees
