from gpiozero import LED, Button
from light_sensor import read_ldr
from time import sleep
from datetime import datetime

led = LED(16)
button = Button(24)
is_running = True
interval = 1000 # in ms
LIGHT_THRESHOLD = 0.6

def on_btn_pressed():
    global is_running
    is_running = not is_running
    print(f"Button pressed. {'Turning on.' if is_running else 'Turning off.'}")

def get_timestamp():
    return int(datetime.now().timestamp() * 1000)

button.when_pressed = on_btn_pressed

while True:
    before_time = get_timestamp()

    if not is_running:
        led.off()
        sleep(interval / 1000)
        continue

    ldr_value = read_ldr()
    if ldr_value < LIGHT_THRESHOLD and led.value == 0:
        led.on()
    elif ldr_value >= LIGHT_THRESHOLD and led.value == 1:
        led.off()

    if not is_running:
        continue

    print(f"Light value: {ldr_value:.2f}")

    after_time = get_timestamp()
    time_buffer = max(0, interval - (after_time - before_time))

    sleep(time_buffer / 1000)