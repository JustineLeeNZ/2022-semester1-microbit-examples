# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:

    # code runs if button A pressed
    if button_a.was_pressed():
        display.show(Image.HEART)
    
