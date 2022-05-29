import sys
import webbrowser


def query_link(lat_in_degree, long_in_degree):
    return f'https://maps.google.com/?q={lat_in_degree},{long_in_degree}'


def open_browser(link: str) -> any:
    webbrowser.open(link)
    sys.exit(0)
