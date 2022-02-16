# choose a random number
from microbit import *
import random

while True:
    if button_a.is_pressed():
        # choose and store random number between 1 and 6
        number = random.randint(1, 6)

        # display random number
        display.show(str(number))

