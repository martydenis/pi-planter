import RPi.GPIO as GPIO # type: ignore

GPIO.setmode(GPIO.BCM)

class Switch:
    gpio_pin = 0

    def __init__(self, pin):
        self.gpio_pin = pin
        GPIO.setup(self.gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.RISING, GPIO.FALLING or GPIO.BOTH
        GPIO.add_event_detect(self.gpio_pin, GPIO.BOTH, callback=self._on_switch, bouncetime=10)

    def _on_switch(self, channel):
        state = GPIO.input(channel)
        print('Switch %s (pin %s)' % ('closed' if state == GPIO.LOW else 'open', channel))

    def kill(self):
        GPIO.remove_event_detect(self.gpio_pin)
