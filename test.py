import RPi.GPIO as GPIO # type: ignore
from components import *
import time
import readchar # type: ignore

FAN_INCREMENT = 10

class Test:
    def __init__(self):
        self.led = Output(18)
        self.ldr = Photoresistor(14)
        self.switch = Switch(16, self._on_switch_change)
        self.pump = Output(27)
        self.fan = Fan(6, 13, 19)
        self.running = True

    def _on_switch_change(self, is_closed):
        if is_closed:
            self.pump.on()
        else:
            self.pump.off()
        print(f"[Switch] {'closed' if is_closed else 'open'}")

    def handle_key(self, key):
        if key == readchar.key.UP:
            self.fan.add_speed(FAN_INCREMENT)
            print(f"[FAN] speed -> {self.fan.speed}%")
        elif key == readchar.key.DOWN:
            self.fan.add_speed(-FAN_INCREMENT)
            print(f"[FAN] speed -> {self.fan.speed}%")
        elif key == "l":
            self.led.toggle()
            print(f"[LED] {self.led.get_state()}")
        elif key == "p":
            self.pump.toggle()
            print(f"[Pump] {self.pump.get_state()}")
        elif key == "r":
            print(f"[LDR] reading = {self.ldr.read()}")
        elif key == "q":
            self.running = False

    def loop(self):
        print("Controls: Up/Down = fan +-10%, l = led, p = pump, r = read ldr, q = quit")
        while self.running:
            key = readchar.readkey()
            self.handle_key(key)
            time.sleep(0.15)

    def cleanup(self):
        print("\nStopping, cleaning up GPIO...")
        self.pump.off()
        self.fan.off()
        GPIO.cleanup()

def main():
    test = Test()
    try:
        test.loop()
    except KeyboardInterrupt:
        test.cleanup()

if __name__ == "__main__":
    main()
