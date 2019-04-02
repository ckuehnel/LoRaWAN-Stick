#!/usr/bin/python3

# Get temperature and pressure from environmental sensor and sends LoRaWAN message to TTN server
# Used hardware: ENVIRO PHAT & Raspberry Pi 3B+ w/ Raspbian Stretch
# Program: EnviroNode.py
# (c) Claus Kuehnel 2019-04-01 info@ckuehnel.ch

import time, sys
from envirophat import weather
from LoRaWAN_TTN import *

unit = 'hPa'  # Pressure unit, can be either hPa (hectopascals) or Pa (pascals)

print('Running EnviroNode.py...\n')

connectTTN()
time.sleep(10)
print('Request measuring data and send them to TTN each 60 sec...\n')

try:
    while True:
        now = time.strftime('%Y-%m-%d %H:%M')
        print(time.strftime(now) + '\t', end='')

        output = 'Temperature = {t:.2f} *C  Pressure = {p:.1f} {unit}'.format(unit=unit, t=weather.temperature(), p=weather.pressure(unit=unit))
        print(output)

        print('Data format to be sent\t', end='')  
        data = '{t:.2f},{p:.1f}'.format(t=weather.temperature(), p=weather.pressure(unit=unit))
        print(data)
        print()

        sendMsg(data)
        print('----------------------------------', end='')
        print('----------------------------------')

        time.sleep(60)

except KeyboardInterrupt:
    pass
