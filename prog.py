import serial

ser = serial.Serial('/dev/ttyAMA1', 115200)
print('serial connection opened')

while True:
	speed = raw_input()
	angle = raw_input()
	command = "speed: " + speed + "angle: " + angle
	ser.write(bytes(command))

ser.close()
print('serial connection closed')
