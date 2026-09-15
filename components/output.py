import RPi.GPIO as GPIO # type: ignore

GPIO.setmode(GPIO.BCM)

class Output:
    gpio_pin = 0

    def __init__(self, pin):
        self.gpio_pin = pin
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        GPIO.output(self.gpio_pin, GPIO.LOW)

    def on(self):
        GPIO.output(self.gpio_pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.gpio_pin, GPIO.LOW)

    def get_state(self):
        return GPIO.input(self.gpio_pin)

    def toggle(self):
        if GPIO.input(self.gpio_pin):
            GPIO.output(self.gpio_pin, GPIO.LOW)
        else:
            GPIO.output(self.gpio_pin, GPIO.HIGH)
