# simple counter

from microbit import *

# create counter variable and set it 0
counter = 0

''' check if button a pressed, add 1 and
display current value '''
while True:
    # if button b pressed, add 1 to counter
    if button_a.is_pressed():
        counter += 1
        display.scroll(str(counter),100)

    # if button b pressed, subtract 1 from counter
    if button_a.is_pressed():
        counter = counter - 1
        display.scroll(str(counter),100)
