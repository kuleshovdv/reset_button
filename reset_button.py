#!/usr/bin/env python2.7
import RPi.GPIO as GPIO
import subprocess
import time

# GPIO chanel for Reset Button
# By default is GP23
chanel = 23

# Pressing time for system reboot
delaySystemReset = 2000

def waitForPress():
	while True:
		GPIO.wait_for_edge(chanel, GPIO.FALLING)
		# Short press for stop running emulator and return to Emulationstation
		subprocess.call("pkill retroarch && nohup emulationstation && pkill mupen64plus &", shell=True,
		                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		timePush = round(time.time() * 1000)
		timePresses = 0
		while GPIO.input(chanel) == GPIO.LOW:
			timePressed = round(time.time() * 1000) - timePush
			if timePressed >= delaySystemReset:
				# When long press
				# System reboot
				subprocess.call("reboot")
				GPIO.cleanup()
				break

if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(chanel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	waitForPress()

