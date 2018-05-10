import struct
import serial
import serial.tools.list_ports

"""Try to get Arduino connected port, if dont, raise error"""
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
	

	
