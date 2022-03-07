# shows random images

from microbit import *
import random


while True:
    if button_a.was_pressed():
        number = random.randint(1,4)
        if number == 1:
            display.show(Image.HAPPY)
        elif number == 2:
            display.show(Image.SAD)
        elif number == 3:
            display.show(Image.HEART)
        elif number == 4:
            display.show(Image.ASLEEP)
