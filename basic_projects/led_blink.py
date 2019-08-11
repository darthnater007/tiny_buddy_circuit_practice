import RPi.GPIO as GPIO
import time

###Breadboard setup
# pin 12- any GPIO <#> works- (out) (j7) to a40
#resistor from  d40 to d34
#led long (+) e34 to short (-) e33
#jumper from b33 to c20 (pin 39- GND) 

ledPin = 11 #GPIO 17

def setup():
	GPIO.setmode(GPIO.BOARD) #this numbers GPIO pins by location (1-40)
	GPIO.setup(ledPin, GPIO.OUT) #pin 11 is an output
	GPIO.output(ledPin, GPIO.LOW) #set pin 11 to off
	print('using pin%d' %ledPin)

def blink():
	while True:
		GPIO.output(ledPin, GPIO.HIGH) #led on
		print('led on')
		time.sleep(1) #wait one second
		GPIO.output(ledPin, GPIO.LOW) #led off
		print('led off')
		time.sleep(1) #wait one second
		#repeat until killed
def destroy():
	GPIO.output(ledPin, GPIO.LOW) #turn off pin 11
	GPIO.cleanup()  #release GPIO resource

if __name__ == '__main__': #program start
	setup()
	try:
		blink()

	except KeyboardInterrupt: #use 'Ctrl+C' to destroy
		destroy()
