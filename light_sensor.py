from gpiozero import OutputDevice, InputDevice
from time import sleep

LDR_PIN = 17
MAX_STEPS = 100      # increase if too dark and always returning 100
STEP_DELAY = 0.01    # 10ms per step = 1 second max charge time

def read_ldr():
    # Discharge capacitor
    ldr = OutputDevice(pin=LDR_PIN, active_high=True, initial_value=False)
    sleep(0.1)
    ldr.close()

    # Switch to input and count charge steps
    ldr = InputDevice(pin=LDR_PIN, pull_up=None, active_state=True)
    count = 0
    for i in range(1, MAX_STEPS + 1):
        if ldr.is_active:
            count = i
            break
        sleep(STEP_DELAY)
    ldr.close()

    # Normalize to 0.0 (dark) -> 1.0 (bright)
    if count == 0:
        return 0.0
    return 1.0 - (count / MAX_STEPS)