import RPi.GPIO as GPIO
import math

class RotaryEncoder:
	""" """
	def __init__(self,a_pin,b_pin):
		self.a_pin = a_pin
		self.b_pin = b_pin
		self.value = 0
		self.last_encoded = 0
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.a_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.b_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
		GPIO.add_event_detect(self.a_pin, GPIO.BOTH)
		GPIO.add_event_callback(self.a_pin, updateEncoders)
		
		GPIO.add_event_detect(self.b_pin, GPIO.BOTH)
		GPIO.add_event_callback(self.b_pin, updateEncoders)
		
		
	"""                           _______         _______       
//               Pin_a ______|       |_______|       |______ Pin_a
// negative <---         _______         _______         __      --> positive
//               Pin_b __|       |_______|       |_______|   Pin_b

		//	old	old	new	new
		//	pin_a	pin_b	pin_a	pin_b	Result
		//	----	----	----	----	------
		//	0	0	0	0	no movement
		//	0	0	0	1	-1
		//	0	0	1	0	+1
		//	0	0	1	1	-2  (assume pin_a edges only)
		//	0	1	0	0	+1
		//	0	1	0	1	no movement
		//	0	1	1	0	+2  (assume pin_a edges only)
		//	0	1	1	1	-1
		//	1	0	0	0	-1
		//	1	0	0	1	+2  (assume pin_a edges only)
		//	1	0	1	0	no movement
		//	1	0	1	1	+1
		//	1	1	0	0	-2  (assume pin_a edges only)
		//	1	1	0	1	+1
		//	1	1	1	0	-1
		//	1	1	1	1	no movement
"""	
	def updateEncoders(self,chan):
		MSB = GPIO.input(self.a_pin);
        LSB = GPIO.input(self.b_pin);

        encoded = (MSB << 1) | LSB;
        sum = (self.lastEncoded << 2) | encoded;

        if(sum == 0b1101 || sum == 0b0100 || sum == 0b0010 || sum == 0b1011) self.value++;
        if(sum == 0b1110 || sum == 0b0111 || sum == 0b0001 || sum == 0b1000) self.value--;
		
		if(sum == 0b0110 || sum == 0b1001) self.value += 2;
        if(sum == 0b0011 || sum == 0b1100) self.value -= 2;

        self.lastEncoded = encoded;
		
	def resetEncoder(self)
		self.value = 0
		self.lastEncoded = 0
		
		