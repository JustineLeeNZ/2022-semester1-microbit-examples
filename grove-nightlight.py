# night light

from microbit import *

display.show(Image.HAPPY)

while True:
    # read the light level
    light_level = pin0.read_analog()

    # check the light level
    if light_level < 100:
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)


