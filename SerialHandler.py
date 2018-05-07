import struct
import serial
import serial.tools.list_ports

class SerialHandler():
	def __init__(self):
		self.ser = serial.Serial()
	def configureSerial(self,port):
		self.ser.baudrate = 9600
		self.ser.port = port

	def sendValues(self,keys):		
			for a in keys:
				self.ser.write(struct.pack('>B', int(a)))
				print(a)
			
		
def getPort():
	arduino_ports = [
		p[0]
		for p in serial.tools.list_ports.comports()
		if 'Arduino' in p[1]
	]

	if not arduino_ports:
		raise IOError    
	else:
		return arduino_ports[0]
	

	
