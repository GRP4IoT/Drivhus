import pigpio
from time import sleep
from gpiozero import Button
from signal import pause
led = LED(17)
#KNAP_GPI_PIN = 4
button = Button(6)
pi = pigpio.pi()
pi.set_PWM_range(led, 100)
#knap = pi.read(KNAP_GPI_PIN)
level = 0
dir = 1


while True:
	if button.is_pressed:
# andlevel >= 99 or level <= 0:
	   pi.set_PWM_dutycycle(LED_GPI_PIN, level)
	   sleep(0.1)
	   level += dir
	elif button.is_released:
             led.off
   #elif level >= 99 or level <= 0:
	#dir = 0
