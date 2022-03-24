# Turn LED on and off

from microbit import *

# listen for events
while True:
    # turn LED on
    if button_a.was_pressed():
        pin0.write_digital(1)
    # turn LED off
    if button_a.was_pressed():
        pin0.write_digital(0)

