""" A whack a Mole game with the goal of 
    measuring the Reaction Time.
"""

# importing needed libs
from psychopy import visual, event
import random

COLORS = ["red","green","blue"]
LOCATIONS = [0.5, 0, -0.5]
TIME_LEFT = [0.75, 1, 1.25, 1.5]
TIME_PRESENTED = [0.5, 0.75]


win1 = visual.Window(size=(800, 600), units="height")
# Visuals
icircle = random.randrange(len(LOCATIONS))
circle = visual.Circle(win1, radius = 0.1, pos = (LOCATIONS[icircle], 0), fillColor=COLORS[icircle])

# main loop
keep_up = True
while keep_up:
    # Visuals
    circle.draw()
    win1.flip()

    # Waiting for key press
    keep_up = len(event.getKeys(keyList=['escape'])) == 0

win1.close()

### 9.9 AND REST REMAINING