# do stuff with music - Justine Lee - 22/2/22

from microbit import *

# need this library to play music
import music

while True:
    # play built-in melody if A+B pressed
    if button_a.is_pressed() and button_b.is_pressed():
        music.play(music.ODE)



    # else if button a pressed, set volume to 50
    elif button_a.is_pressed():
        set_volume(50)

    # else if button b pressed, set volume to 200
    elif button_b.is_pressed():
        set_volume(200)





