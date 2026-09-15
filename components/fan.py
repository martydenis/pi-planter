import RPi.GPIO as GPIO # type: ignore
from time import sleep


class Fan:
    pwm_frequency = 500
    pulses_per_revolution = 2
    pulse_count = 0
    speed = 0

    def __init__(self, base_pin, pwm_pin, rpm_pin):
        self.base_pin = base_pin
        self.pwm_pin = pwm_pin
        self.rpm_pin = rpm_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.base_pin, GPIO.OUT)
        GPIO.output(self.base_pin, GPIO.LOW)  # start with fan off

        GPIO.setup(self.rpm_pin, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
        GPIO.add_event_detect(self.rpm_pin, GPIO.RISING, callback=self._count_pulse, bouncetime=20)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, self.pwm_frequency)
        self.pwm.start(0)

    def set_speed(self, speed: int):
        self.speed = max(0, min(100, speed))
        if self.speed == 0:
            self.off()
        else:
            if GPIO.input(self.base_pin) == GPIO.LOW:
                self.on()
            self.pwm.ChangeDutyCycle(self.speed)

    def add_speed(self, value: 10):
        self.set_speed(max(0, min(100, self.speed + value)))

    def on(self):
        GPIO.output(self.base_pin, GPIO.HIGH)
        self.pwm.start(0)

    def off(self):
        self.pwm.stop()
        GPIO.output(self.base_pin, GPIO.LOW)

    def get_rpm(self):
        self.pulse_count = 0
        sleep(1)
        return int((self.pulse_count / self.pulses_per_revolution) * 60)

    def _count_pulse(self, pin):
        self.pulse_count += 1
