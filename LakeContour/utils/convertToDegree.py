# convert raw NMEA string into degree decimal format
def convert_to_degrees(raw_value):
    decimal_value = raw_value / 100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - degrees) / 0.6
    position = degrees + mm_mmmm
    return "%.9f" % position
