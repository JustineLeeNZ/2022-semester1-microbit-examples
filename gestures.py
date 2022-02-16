# detect gestures (uses accelerometer)

from microbit import *

# loop forever
while True:

    # get value of current gesture
    gesture = accelerometer.current_gesture()


    # display image based on gesture
    #face up is HAPPY
    if gesture == "face up":
        display.show(Image.HAPPY)

    elif gesture == "left":
        display.show(Image.SAD)

    # anything else is ANGRY
    else:
        display.show(Image.ANGRY)

