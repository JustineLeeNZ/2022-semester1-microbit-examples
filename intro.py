# Write your code here :-)
from microbit import *

display.scroll("Hello world")
# show inbuilt image
display.show(Image.HAPPY)

# show DIY image
# create DIY image
boat = Image("05050:"
             "05050:"
            "05050:"
            "99999:"
           "09990")

#display DIY image
display.show(boat)
