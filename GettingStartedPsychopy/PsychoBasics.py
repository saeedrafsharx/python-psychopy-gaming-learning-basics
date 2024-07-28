"""
A minimal PsychoPy code.
"""

# this imports two modules from psychopy
# visual has all the visual stimuli, including the Window class
# that we need to create a program window
# event has function for working with mouse and keyboard
from psychopy import visual, event
import random
game_over = True
# creating a 800 x 600 window
window1 = visual.Window(size=(800, 600), units= "norm")
text_stimulus = visual.TextStim(window1,  "Press Escape to Exit", color=(1,0,1), bold = True)
sqr1 = visual.Rect(window1, pos = (0,-0.65))

while game_over:
    text_stimulus.draw()
    sqr1.draw()
    window1.flip()
    key = event.getKeys(['escape', 'space'])
    if len(key) > 0:

        if key[0] == "space":
            sqr1.pos = (random.uniform(-1,1), random.uniform(-1,1))
        else:
            game_over = False

window1.close()  