# do stuff with music - Justine Lee - 22/2/22

from microbit import *

# need this library to play music
import music

# play own melody
# create list of notes in tune
tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4",
        "E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]
# play tune
music.play(tune)

