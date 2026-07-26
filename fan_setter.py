from gpiozero import PWMOutputDevice
from time import sleep

# TODO: use pigpio lib instead of PWMOutputDevice
fan = PWMOutputDevice(pin=17, initial_value=0, frequency=2000)

fan.on()

def set_fan_speed(speed: float):
    global fan
    fan.value = speed
    print(f"Fan speed: {(speed * 100):.0f}%")

try:
    while True:
        set_fan_speed(0)
        sleep(20)
        set_fan_speed(1)
        sleep(20)
        set_fan_speed(0.10)
        sleep(20)
        set_fan_speed(1)
        sleep(20)
        fan.off()
except KeyboardInterrupt:
    pass
