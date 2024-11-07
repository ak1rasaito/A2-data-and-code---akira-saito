import audio
import random
from microbit import *

#volume 
set_volume(255) 

# Read the files from the micro:bit filesystem
def read_frame(file, frame):
    ln = file.readinto(frame)
    while ln:
        yield frame
        ln = file.readinto(frame)
        
# create a function to open and play each file in turn
def play_file(f):
    frame = audio.AudioFrame()
    with open(f, "rb") as file:
        audio.play(read_frame(file, frame), wait=True)

# List of audio files
phrases = [
    "I am brave.raw",
    "I am kind.raw",
    "I am a good friend.raw",
    "I am helpful.raw",
    "I am loved.raw", 
    "I am smart.raw", 
    "I am strong.raw", 
    "I am super.raw", 
    "I love others.raw"
    
]

last_phrase = ""

# audio plays when button is pressed
while True:
    if pin0.is_touched():
        # Select a random phrase that is not the same as the last one
        phrase = random.choice(phrases)
        while phrase == last_phrase:
            phrase = random.choice(phrases)
        last_phrase = phrase  # Update last played to the most recent played

        # Play the selected phrase file
        play_file(phrase)

#sound effects on shake 
    if accelerometer.was_gesture('shake'):
        audio.play(Sound.GIGGLE)
            
