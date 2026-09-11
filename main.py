import RPi.GPIO as GPIO # type: ignore
from components import *
import time
from datetime import datetime

INTERVAL = 2000 # in ms
LIGHT_THRESHOLD = 0.6

def get_timestamp():
    return int(datetime.now().timestamp() * 1000)

def main():
    led = Output(18)
    ldr = Photoresistor(14)
    switch = Switch(16)
    pump = Output(27)

    pump.on()
    print("Pump on")

    try:
        while True:
            # before_time = get_timestamp()

            ldr_value = ldr.read()
            print(f"Light value: {ldr_value:.2f}")
            if ldr_value < LIGHT_THRESHOLD:
                led.on()
            elif ldr_value >= LIGHT_THRESHOLD:
                led.off()

            # pump.on()
            # print("Pump on")
            # time.sleep(5)
            # print("Pump off")
            # pump.off()

            time.sleep(5)

            # after_time = get_timestamp()
            # buffer = max(0, INTERVAL - (after_time - before_time))
            # time.sleep(buffer / 1000)
    except KeyboardInterrupt:
        print("\nStopping, cleaning up GPIO...")
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
