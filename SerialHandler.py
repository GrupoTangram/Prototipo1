import serial
import struct
import serial.tools.list_ports
ARDUINO_STATUS = True;
arduino_ports = []
def getLabel():
	global ARDUINO_STATUS
	global	arduino_ports

	arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description
	]

	if not arduino_ports:
		ARDUINO_STATUS = False
		return "Nenhum dispositivo conectado!"       
	else:
		ARDUINO_STATUS = True
		return "Dispositivo conectado!"

def sendValues(keys):
	if(ARDUINO_STATUS == True):
		ser = serial.Serial(arduino_ports[0],9600)
		for a in keys:
			ser.write(a)
	else:
		raise noArduino(ARDUINO_STATUS)


class noArduino(Exception):
	def __init__(self,msg):
		super().__init__(msg)






	
