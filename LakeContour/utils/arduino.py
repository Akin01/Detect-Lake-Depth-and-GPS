import serial


def connect(port: str):
    return serial.Serial(port)


def parseData(serial_connect: any, *args, **kwargs) -> list:
    gpgga_info = kwargs['gpgga_info']

    received_data = seria_connect.readline().decode()  # read NMEA string received
    GPGGA_data_available = received_data.find(gpgga_info)  # check for NMEA GPGGA string

    if GPGGA_data_available > 0:
        GPGGA_buffer = received_data.split(gpgga_info, 1)[1]  # store data coming after "$GPGGA," string
        NMEA_buff = GPGGA_buffer.split(',')  # store comma separated data in buffer

        return NMEA_buff
