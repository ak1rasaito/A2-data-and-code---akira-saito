#audio plays when button pressed
from microbit import *
import music


while True:
    if button_a.was_pressed():
        music.play(music.BA_DING)




