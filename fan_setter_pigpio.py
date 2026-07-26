import pigpio
from time import sleep

pi = pigpio.pi()
FAN_PIN = 17

def set_fan_speed(speed: float):
    # Set the duty cycle (0 to 255)
    pwm_speed = int(speed * 255)
    pi.set_PWM_dutycycle(FAN_PIN, pwm_speed)
    print(f"Fan speed: {(speed * 100):.0f}%")

try:
    while True:
        set_fan_speed(0)
        sleep(15)
        set_fan_speed(1)
        sleep(15)
        set_fan_speed(0.10)
        sleep(15)
        set_fan_speed(1)
        sleep(15)
       
except KeyboardInterrupt:
    pass
finally:
    pi.stop()
