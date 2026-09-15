import RPi.GPIO as GPIO # type: ignore

GPIO.setmode(GPIO.BCM)

class Switch:
    gpio_pin = 0

    def __init__(self, pin, callback: None):
        self.gpio_pin = pin
        self.callback = callback
        GPIO.setup(self.gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.RISING, GPIO.FALLING or GPIO.BOTH
        GPIO.add_event_detect(self.gpio_pin, GPIO.BOTH, callback=self._on_switch, bouncetime=10)

    def set_callback(self, callback):
        self.callback = callback

    def _on_switch(self, channel):
        state_closed = GPIO.input(channel) == GPIO.LOW

        if self.callback:
            self.callback(state_closed)

    def kill(self):
        GPIO.remove_event_detect(self.gpio_pin)
