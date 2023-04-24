import pygeoip
import urllib.request, json

gi = pygeoip.GeoIP('GeoLiteCity.dat')
def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    cont = rec['continent']
    country = rec['country_name']
    long = rec['longitude']