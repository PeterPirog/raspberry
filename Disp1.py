#https://pifacecad.readthedocs.io/en/latest/example.html

import pifacecad
import time
cad = pifacecad.PiFaceCAD()    # create PiFace Control and Display object
cad.lcd.backlight_on()         # turns the backlight on
cad.lcd.write("Dzien Dobry Ilonko") # writes hello world on to the LCD
while 1:
    cad.lcd.move_right()
    time.sleep(0.2)

""" CURSOR CONTROL
cad.lcd.set_cursor(4, 1)  # set the cursor to col 4 on the second row
cad.lcd.cursor_off()      # turns the cursor off
cad.lcd.write("3.141592") # writes π to the LCD

cad.lcd.blink_off()       # turns the blinking off
cad.lcd.cursor_on()       # turns the cursor on
cad.lcd.home()            # send the cursor home

cad.lcd.write("PiFace Control\nand Display")  # '\n' starts a new line
cad.lcd.clear()           # clear the screen (also sends the cursor home)


>>> cad.lcd.write("Something really, really long.")
>>> cad.lcd.move_right()
>>> cad.lcd.move_left()
>>> cad.lcd.see_cursor()  # move the display so that we can see the cursor

"""


