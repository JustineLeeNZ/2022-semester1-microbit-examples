# use radio block to send an image

from microbit import *

# need this to use radio
import radio

# turn the radio
radio.on()

# set radio group
radio.config(group=1)

while True:
    if accelerometer.was_gesture('shake'):
        display.clear()
        radio.send('duck')

    message = radio.receive()
    if message == 'duck':
        display.show(Image.DUCK)




