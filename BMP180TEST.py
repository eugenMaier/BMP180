#Eugen Maier
#ETS 2021




from bmp180 import BMP180
from machine import I2C, Pin            # create an I2C bus object accordingly to the port you are using
import math
import time

bus = I2C(scl=Pin(22), sda=Pin(21), freq=100000)           # on pyboard
# bus =  I2C(scl=Pin(4), sda=Pin(5), freq=100000)   # on esp8266
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

while True:                                             #Setzt eine Schleife

    temp = bmp180.temperature
    p = bmp180.pressure /100
    altitude = bmp180.altitude

    print("\n\n")                                       #\n steht für Nächste zeile, somit macht er immer 2 Leerzeichen
    print("Die Temperatur betraegt %d \u00b0C"%temp)    # \u00b0 Steht für ° , sonst macht er ein Fehler   %d als Ganz Zahl ausgeben, gibt Temperatur aus

    print("Der Luftdruck betraegt %d hPa"%p)            # gibt Luftdruck aus
    print("Hoehe %d m" %altitude)

    time.sleep(10)                                      # Wartet 10s bis der Loop sich wiederholt
