
#!/usr/bin/env python3
"""
Simple GPIO test script for switching a 12V light on/off
through a 2N2222 transistor via GPIO18.
"""

import RPi.GPIO as GPIO
import time

LIGHT_PIN = 4  # BCM numbering, physical pin 11

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LIGHT_PIN, GPIO.OUT)
    GPIO.output(LIGHT_PIN, GPIO.LOW)  # start with light off

def light_on():
    GPIO.output(LIGHT_PIN, GPIO.HIGH)
    print("Light ON")

def light_off():
    GPIO.output(LIGHT_PIN, GPIO.LOW)
    print("Light OFF")

def main():
    setup()
    try:
        while True:
            light_on()
            time.sleep(5)
            light_off()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nStopping test, cleaning up GPIO...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
