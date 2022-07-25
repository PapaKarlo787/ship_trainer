from serial import *
import serial.tools.list_ports

class Manipulator():
	def __init__(self, n):
		ports = serial.tools.list_ports.comports()
		print(ports[0])
		self.port = Serial("/dev/ttyACM0", 115200)
		self.n = n

	def get_data(self):
		self.port.write(bytes([self.n * 2]))
		while (not self.port.in_waiting):
			pass
		x = self.port.read()
		y = self.port.read()
		return (y[0]/256, (0.5 - x[0]/256)/4)
