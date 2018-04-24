import serial
import struct
import serial.tools.list_ports

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description
]
if not arduino_ports:
    print("Nenhum Arduino conectado!")
    
ser = serial.Serial(arduino_ports[0], 9600)

for a in range(3):
    ser.write(struct.pack('>B', int(input("valor do %d botão: " %(a+1)))))
