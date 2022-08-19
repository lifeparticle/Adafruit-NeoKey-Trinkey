# https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/NeoKey_Trinkey/CircuitPython_HID_Cap_Touch_Example/code.py

import time
import board
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode  # pylint: disable=unused-import
from digitalio import DigitalInOut, Pull
import touchio

print("NeoKey Trinkey HID")

# create the pixel and turn it off
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)
pixel.fill(0x0)

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

# create the switch, add a pullup, start it with not being pressed
button = DigitalInOut(board.SWITCH)
button.switch_to_input(pull=Pull.DOWN)
button_state = False

# create the captouch element and start it with not touched
touch = touchio.TouchIn(board.TOUCH)
touch_state = False

# print a string on keypress
key_output = (
   {'keys': (Keycode.COMMAND, Keycode.SPACEBAR), 'delay': 0.1},
   {'keys': "iterm\n", 'delay': 1},  # give it a moment to launch!
   {'keys': "cd path_to_your_shell_script", 'delay': 0.1},
   {'keys': "./neokey_trinkey_script.sh", 'delay': 0.1},
   {'keys': Keycode.ENTER, 'delay': 0.1},
)

# our helper function will press the keys themselves
def make_keystrokes(keys, delay):
    if isinstance(keys, str):  # If it's a string...
        keyboard_layout.write(keys)  # ...Print the string
    elif isinstance(keys, int):  # If its a single key
        keyboard.press(keys)  # "Press"...
        keyboard.release_all()  # ..."Release"!
    elif isinstance(keys, (list, tuple)):  # If its multiple keys
        keyboard.press(*keys)  # "Press"...
        keyboard.release_all()  # ..."Release"!
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
                make_keystrokes(k['keys'], k['delay'])
        else:
            make_keystrokes(key_output, delay=0)
        button_state = False
