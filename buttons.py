# using buttons as inputs

from microbit import *

# loops forever
while True:
    # if button A pressed, show happy face
    if button_a.is_pressed():
        display.show(Image.HAPPY)


    # if button b pressed, show sad face
    if button_b.is_pressed():
        display.show(Image.SAD)






