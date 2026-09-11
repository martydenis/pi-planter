import RPi.GPIO as GPIO # type: ignore
import time

GPIO.setmode(GPIO.BCM)
MAX_STEPS = 100      # increase if too dark and always returning 100
STEP_DELAY = 0.01    # 10ms per step = 1 second max charge time

class Photoresistor:
    pin = 0

    def __init__(self, pin):
        self.pin = pin

    def read(self):
        # Discharge capacitor
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(0.1)

        # Switch to input and count charge steps
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

        # ldr = InputDevice(pin=self.pin, pull_up=None, active_state=True)
        count = 0
        for i in range(1, MAX_STEPS + 1):
            if GPIO.input(self.pin) == GPIO.HIGH:
                count = i
                break
            time.sleep(STEP_DELAY)

        # Normalize to 0.0 (dark) -> 1.0 (bright)
        if count == 0:
            return 0.0
        return 1.0 - (count / MAX_STEPS)
