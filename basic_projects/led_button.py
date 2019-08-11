import RPi.GPIO as GPIO

ledPin = 11 #GPIO 17
buttonPin = 12 #GPIO 18

def setup():
	print('starting led_button.py')
	GPIO.setmode(GPIO.BOARD) #numbers GPIO by physical location  (1-40)
	GPIO.setup(ledPin, GPIO.OUT) #pin 11 is out
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
	#The pull-up/downs supply that voltage so that the gpio will have a defined 
	#value UNTIL overridden by a stronger force.

 	#You should set a pull-down (to 0) when you expect the
 	#stronger force to pull it up to 1.

	#You should set a pull-up (to 1) when you expect the 
 	#stronger force to pull it down to 0.

def loop():
	while True:
		if GPIO.input(buttonPin) == GPIO.LOW:
			GPIO.output(ledPin, GPIO.HIGH)
			print('LED: On')
		else:
			GPIO.output(ledPin, GPIO.LOW)
			print('LED: Off')

def destroy():
	GPIO.output(ledPin, GPIO.LOW)
	GPIO.cleanup()

if __name__ == '__main__': #Start Program

	setup()

	try:

		loop()
	except KeyboardInterrupt: #CTRL C to quit

		destroy()
