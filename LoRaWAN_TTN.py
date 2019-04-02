#!/usr/bin/python3

import serial, time

ser=serial.Serial('/dev/ttyUSB0', 115200, timeout=10)

def writeCmd(cmd):
    ser.write(cmd)
    try:
        while True:
            response = ser.readline()
            print("Response:", response)
            if b'OK' in response:
                break
    except KeyboardInterrupt:
        pass

def testCmd(cmd):
    print('\n' + cmd.decode()[:-2])
    writeCmd(cmd)

def sendMsg(msg):
    msg = ('AT+NCMGS=' + str(len(msg)) + ',' + msg + '\r\n')
    testCmd(str.encode(msg))
    
def connectTTN():
    print('\nInit LoRaWAN and connect to TTN...')

    testCmd(b'AT+NRB\r\n')
    testCmd(b'AT+NCONFIG\r\n')
    testCmd(b'AT+DEVEUI\r\n')
    testCmd(b'AT+APPEUI\r\n')
    testCmd(b'AT+APPKEY=28C440A79FEB7899D794DBA5DD8CA207\r\n')
    testCmd(b'AT+CFM=0\r\n')
    testCmd(b'AT+ACTIVATE=1\r\n')
    testCmd(b'AT+SAVE\r\n')

    print('Initialization done.\r\n')

