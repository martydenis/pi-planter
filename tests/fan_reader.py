from gpiozero import DigitalInputDevice
from time import sleep

TACH_PIN = 4
PULSES_PER_REV = 2

tach = DigitalInputDevice(TACH_PIN, pull_up=True, bounce_time=None)  # bounce_time=None disables debouncing

pulse_count = 0

def count_pulse():
    global pulse_count
    pulse_count += 1

tach.when_activated = count_pulse  # Triggered on rising edge

while True:
    pulse_count = 0
    sleep(1)
    rpm = (pulse_count / PULSES_PER_REV) * 60
    print(f"Fan speed: {rpm:.0f} RPM")
