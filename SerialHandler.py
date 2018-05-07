import struct

import serial
import serial.tools.list_ports

ser = serial.Serial("COM13",9600)

class SerialHandler():
	def __init__(self):
		self.ARDUINO_STATUS = True
		self.ser = None

	def tryConnection(self):
	
		arduino_ports = [
			p[0]
			for p in serial.tools.list_ports.comports()
			if 'Arduino' in p[1]
		]
		
		if not arduino_ports:
			self.ARDUINO_STATUS = False
			return "Nenhum dispositivo conectado!"       
		else:
			self.ARDUINO_STATUS = True
			self.ser = serial.Serial(arduino_ports[0], 9600)
			return "Dispositivo conectado!"
			

	def sendValues(self,keys):		
		if(self.ARDUINO_STATUS == True):
			for a in keys:
				ser.write(struct.pack('>B', int(a)))
				print(a)
			
		else:
			raise IOError("Nenhum Arduino encontrado")
