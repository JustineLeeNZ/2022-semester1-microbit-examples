''' check servo horn is in correct place '''

from microbit import *

# show that code has loaded
display.show(Image.SQUARE_SMALL)

# set up PWM
pin0.set_analog_period(20)


while True:
    if button_a.was_pressed():

        # show that have entered if statement
        display.show(Image.YES)

        # move servo attached to pin0 to 90 degrees
        pin0.write_analog(90)
        sleep(250)

        # turn the servo off
        pin0.write_digital(0)


