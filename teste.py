import serial

ser = serial.Serial("COM13",9600)
ser.write(b'a')

