
#constant
COL0 		= 0
COL1 		= 56
COL2 		= 63
COL3 		= 118
COL4 		= 125
decay 		= .75
MAX_HEIGHT 	= 25
LED_STRIP_LEN 	= 160

from random import randint
import time

#Load driver for your hardware, visualizer just for example
from bibliopixel.drivers.LPD8806 import DriverLPD8806
driver = DriverLPD8806(num = LED_STRIP_LEN)

#load the LEDStrip class
from bibliopixel.led import *
led = LEDStrip(driver)

#load some cool shit right her'
from strip_animations import *
#anim = Rainbow(led)

from bibliopixel.colors import *
mycolors = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.PapayaWhip, colors.Blue, colors.Purple, colors.Pink, colors.Honeydew, colors.Chocolate,
		colors.NavajoWhite, colors.Olive, colors.DarkSalmon, colors.IndianRed, colors.Navy, colors.SeaGreen]

#anim = Rainbow(led)
#anim = FireFlies(led, mycolors) 
#anim = PartyMode(led, colors.hue_spectrum)
#anim = LarsonScanner(led, colors.Green)
#anim = WaveMove(led, colors.Green, 3000)
#anim = ColorWipe(led, colors.Green)
#anim = ColorFade(led, colors.hue_rainbow)
#anim = RainbowCycle(led)
#anim = LarsonRainbow(led)

def display_column(col, color=colors.Purple):
	global columns
	
	if col == 0:
		height = randint(1, MAX_HEIGHT)	
	else:
		c = columns[col-1]
		c = int(round(c))
		if c < 6:
			minRand = 1
		else:
			minRand = c - 5
		if c > MAX_HEIGHT - 5:
			maxRand = MAX_HEIGHT
		else:
			maxRand = c + 5

		height = randint(minRand, maxRand)
		
	if height < columns[col]:
		columns[col] = columns[col] * decay
		height = columns[col]
	else:
		columns[col] = height

	#print height

	if col == 0:
		led.fill(colors.Off, COL0, MAX_HEIGHT)
		led.fill(color, COL0, int(round(height)))
	elif col == 1:
		led.fill(colors.Off, COL1-MAX_HEIGHT, COL1)
		led.fill(color, COL1 - int(round(height)), COL1)
	elif col == 2:
		led.fill(colors.Off, COL2, COL2 + MAX_HEIGHT)
		led.fill(color, COL2, COL2 + int(round(height)))
	elif col == 3:
		led.fill(colors.Off, COL3 - MAX_HEIGHT, COL3)
		led.fill(color, COL3 - int(round(height)), COL3)
	elif col == 4:
		led.fill(colors.Off, COL4, COL4 + MAX_HEIGHT)
		led.fill(color, COL4, COL4 + int(round(height)))

	else:
		print "Index out of range!"

def sigterm_handler(_signo, _stack_frame)
	led.all_off()
	led.update()
	sys.exit(0)

try:
	signal.signal(signal(signal.SIGTERM, sigterm_handler)
	#anim.run()

	#led.fill(colors.Green, COL0, MAX_HEIGHT)
	#second channel need to think backwards
	#led.fill(colors.Blue, COL1-MAX_HEIGHT, COL1)
	#led.fill(colors.Orange, COL2, COL2+MAX_HEIGHT)
	#led.fill(colors.Yellow, COL3-MAX_HEIGHT, COL3)
	#led.fill(colors.Purple, COL4, COL4+MAX_HEIGHT)
	#led.update()
	
	color = colors.Purple
	start = time.time()
	columns = [0, 0, 0, 0, 0]
	while (True):
		elapsed = time.time()
		if elapsed > start + 2:
			end = len(mycolors) - 1
			color = mycolors[randint(0, end)]
			#print "Color index: " + str(color)
			start = time.time()

		display_column(0, color)
		display_column(1, color)
		display_column(2, color)
		display_column(3, color)
		display_column(4, color)
		led.update()
		
		time.sleep(.15)

except KeyboardInterrupt:
	led.all_off()
	led.update()

