# do stuff with music - Justine Lee - 22/2/22

from microbit import *

# need this library to play music
import music

# play simple sound effect

#play a sound effect - concert A for 1 second
music.pitch(440,1000)

# changes pitch as accelerometer titled
while True:
    music.pitch(accelerometer.get_x(), 20)

