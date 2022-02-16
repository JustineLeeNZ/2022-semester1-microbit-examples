# choosing random values
from microbit import *

# need this if you want random numbers or values
import random

# create a list of animals
animals = ["Cat", "Dog", "Elephant", "Drop Bear"]

#choose and display random name
display.scroll(random.choice(animals))

