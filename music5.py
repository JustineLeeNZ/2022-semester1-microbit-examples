# do stuff with music - Justine Lee - 22/2/22

from microbit import *

# need this library to play music
import audio
import music

set_volume(255)

while True:
    # play an expressive sound
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        audio.play(Sound.HAPPY)

    if button_b.is_pressed():
        display.show(Image.SAD)
        audio.play(Sound.SAD)

    if pin_logo.is_touched():
        display.show(Image.SURPRISED)
        audio.play(Sound.SPRING)



