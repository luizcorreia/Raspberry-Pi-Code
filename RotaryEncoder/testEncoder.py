import RotaryEncoder as Encoder

A_PIN = 7
B_PIN = 9

encoder = Encoder.RotaryEncoder(A_PIN,B_PIN)
while True:
	encoder.updateEncoders()
	value = encoder.get_value()
	print "Value: %d" % value