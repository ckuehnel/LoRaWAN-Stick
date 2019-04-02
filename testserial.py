import serial, time

print('Serial Test')

ser=serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
print('\nInterface parameters:')
print(ser)


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
    

print('\nTest serial commands for MEK-D8945AL')

testCmd(b'AT\r\n')
testCmd(b'AT+NRB\r\n')
testCmd(b'AT+INFO\r\n')
testCmd(b'AT+NCONFIG\r\n')
testCmd(b'AT+DEVEUI\r\n')
testCmd(b'AT+APPEUI\r\n')
testCmd(b'AT+APPKEY=28C440A79FEB7899D794DBA5DD8CA207\r\n')
testCmd(b'AT+APPSKEY\r\n')
testCmd(b'AT+NWKSKEY\r\n')
testCmd(b'AT+ADDR\r\n')
testCmd(b'AT+CFM=0\r\n')
testCmd(b'AT+ACTIVATE=1\r\n')
testCmd(b'AT+SAVE\r\n')
time.sleep(5)
testCmd(b'AT+NCMGS=5,Hello\r\n')
time.sleep(5)
sendMsg('Hello World')
