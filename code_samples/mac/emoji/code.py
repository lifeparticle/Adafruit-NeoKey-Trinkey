import time
import board
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Pull
import touchio

print("NeoKey Trinkey HID")

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)
pixel.fill(0x0)

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

button = DigitalInOut(board.SWITCH)
button.switch_to_input(pull=Pull.DOWN)
button_state = False

touch = touchio.TouchIn(board.TOUCH)
touch_state = False

key_output = (
   {'keys': (Keycode.CONTROL, Keycode.COMMAND, Keycode.SPACEBAR), 'delay': 0.2},
   {'keys': "coffee\n", 'delay': 0.5},
   {'keys': [Keycode.DOWN_ARROW, Keycode.ENTER], 'delay': 0.05},
)

def make_keystrokes(keys, delay):
    if isinstance(keys, str):
        keyboard_layout.write(keys)
    elif isinstance(keys, int):
        keyboard.press(keys)
        keyboard.release_all()
    elif isinstance(keys, (list, tuple)):
        keyboard.press(*keys)
        keyboard.release_all()
    time.sleep(delay)

while True:
    if button.value and not button_state:
        pixel.fill((255, 0, 255))
        print("Button pressed.")
        button_state = True

    if not button.value and button_state:
        pixel.fill(0x0)
        print("Button released.")
        if isinstance(key_output, (list, tuple)) and isinstance(key_output[0], dict):
            for k in key_output:
                if isinstance(k['keys'], list):
                    for i in k['keys']:
                        make_keystrokes(i, k['delay'])
                else:
                     make_keystrokes(k['keys'], k['delay'])
        else:
            make_keystrokes(key_output, delay=0)
        button_state = False
