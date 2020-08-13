#https://pifacecad.readthedocs.io/en/latest/example.html

import pifacecad
import time

text="Hello world"

cad = pifacecad.PiFaceCAD()    # create PiFace Control and Display object
cad.lcd.clear()           # clear the screen (also sends the cursor home)
time.sleep(0.2)
cad.lcd.backlight_on()         # turns the backlight on
cad.lcd.write(text) # writes hello world on to the LCD
print(text)

while 1:
    #cad.lcd.move_left()
    time.sleep(0.2)
    cad.lcd.clear()
    button0 = cad.switches[0].value
    button1=cad.switches[1].value
    button2 = cad.switches[2].value
    button3 = cad.switches[3].value
    button4 = cad.switches[4].value
    full_text=button0,button1,button2,button3,button4
    cad.lcd.write(str(full_text))

    print(full_text)
    pass
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


