# stepcounter

from microbit import *

# create variable to record steps
steps = 0

''' check if step taken. If yes, display smile and
add 1 to steps. If button a pressed show number of
steps '''

while True:
    if accelerometer.was_gesture('shake'):
        steps += 1
        display.show(Image.HAPPY)
        sleep(500)
        display.clear()

    if button_a.is_pressed():
        display.show(str(steps))
        sleep(500)
        display.clear()



