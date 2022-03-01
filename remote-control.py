# detect when microbit tilted and send info to partner's microbit

from microbit import *

# set up the radio
import radio

radio.on()

# set radio group
radio.config(group=1)

# loop forever
while True:
    # get value of current gesture
    gesture = accelerometer.current_gesture()

    # display image based on gesture
    #tilt logo left is left arrow (west)
    if accelerometer.was_gesture('left'):
        display.show(Image.ARROW_W)
        radio.send('left')

    # tilt logo right is right arrow (east)
    if accelerometer.was_gesture('right'):
        display.show(Image.ARROW_E)
        radio.send('right')

    # tilt logo up is up arrow (north)
    if accelerometer.was_gesture('up'):
        display.show(Image.ARROW_N)
        radio.send('up')

    # tilt logo down is down arrow (south)
    if accelerometer.was_gesture('down'):
        display.show(Image.ARROW_S)
        radio.send('down')




