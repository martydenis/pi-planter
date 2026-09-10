
#!/usr/bin/env python3
"""
Simple GPIO test script for switching a 12V fan on/off
through a 2N2222 transistor via GPIO18.
"""

import RPi.GPIO as GPIO
import time

FAN_PIN = 17  # BCM numbering, physical pin 11

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT)
    GPIO.output(FAN_PIN, GPIO.LOW)  # start with fan off

def led_on():
    GPIO.output(FAN_PIN, GPIO.HIGH)
    print("Fan ON")

def led_off():
    GPIO.output(FAN_PIN, GPIO.LOW)
    print("Fan OFF")

def main():
    setup()
    try:
        while True:
            led_on()
            time.sleep(10)
            led_off()
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nStopping test, cleaning up GPIO...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
