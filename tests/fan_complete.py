import RPi.GPIO as GPIO # type: ignore
from time import sleep


class Fan:
    pin_power = 17

    pin_setter = 27 # Needs to be a PWM specific GPIO pin
    pwm_frequency = 500

    pin_reader = 22
    pulses_per_revolution = 2
    pulse_count = 0

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_power, GPIO.OUT)
        GPIO.output(self.pin_power, GPIO.LOW)  # start with fan off

        GPIO.setup(self.pin_reader, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
        GPIO.add_event_detect(self.pin_reader, GPIO.RISING, callback=self.count_pulse, bouncetime=20)
        GPIO.setup(self.pin_setter, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin_setter, self.pwm_frequency)
        self.pwm.start(0)

    def set_speed(self, speed: int):
        speed = max(0, min(100, speed))
        if speed == 0:
            self.turn_off()
        else:
            current_rpm = self.get_rpm()
            if GPIO.input(self.pin_power) == GPIO.LOW:
                self.turn_on()
            self.pwm.ChangeDutyCycle(speed)
            # print(f"Setting speed at {speed}%")
            print(f"Current speed: {current_rpm}rpm. Setting speed at {speed}%")

    def turn_on(self):
        GPIO.output(self.pin_power, GPIO.HIGH)
        self.pwm.start(0)
        print("Fan ON")

    def turn_off(self):
        self.pwm.stop()
        GPIO.output(self.pin_power, GPIO.LOW)
        print("Fan OFF")

    def get_rpm(self):
        self.pulse_count = 0
        sleep(1)
        return int((self.pulse_count / self.pulses_per_revolution) * 60)

    def count_pulse(self, pin):
        self.pulse_count += 1

def main():
    fan = Fan()
    try:
        while True:
            fan.set_speed(40)
            sleep(15)
            fan.set_speed(1)
            sleep(15)
            fan.set_speed(100)
            sleep(15)
            fan.set_speed(0)
            sleep(15)
    except KeyboardInterrupt:
        print("\nStopping test, cleaning up GPIO...")
    finally:
        fan.turn_off()
        GPIO.cleanup()


if __name__ == "__main__":
    main()
