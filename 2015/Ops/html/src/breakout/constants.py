# breakoutGraphics.py
# Wantagh techDay - CS.003 Lecture 3
# Created by:   Peter Mountanos
# Modified from: Walker White (Cornell University)
# Date Created:  11/19/13
# Last Modified: 11/20/13

"""Constants module for the final project of CS.003, Breakout.

			*** DO NOT EDIT THE CODE IN THIS FILE ***
"""

import colormodel

# CONSTANTS

# Width of the game display (all coordinates are in pixels)
GAME_WIDTH  = 480
# Height of the game display
GAME_HEIGHT = 620

# Width of the paddle
PADDLE_WIDTH = 58
# Height of the paddle
PADDLE_HEIGHT = 11
# Distance of the (bottom of the) paddle up from the bottom
PADDLE_OFFSET = 30

# Horizontal separation between bricks
BRICK_SEP_H = 5
# Vertical separation between bricks
BRICK_SEP_V = 4
# Height of a brick
BRICK_HEIGHT = 8
# Offset of the top brick row from the top
BRICK_Y_OFFSET = 70

# Number of bricks per row
BRICKS_IN_ROW = 10
# Number of rows of bricks, in range 1..10.
BRICK_ROWS = 10
# Width of a brick
BRICK_WIDTH = GAME_WIDTH / BRICKS_IN_ROW - BRICK_SEP_H

# Diameter of the ball in pixels
BALL_DIAMETER = 18

# Number of attempts in a game
NUMBER_TURNS = 3

# Basic game states
# Game has not started yet
STATE_INACTIVE = 0
# Game is active, but waiting for next ball
STATE_PAUSED   = 1
# Ball is in play and being animated
STATE_ACTIVE   = 2
# Game is over, deactivate all actions
STATE_COMPLETE = 3

# ADD MORE CONSTANTS (PROPERLY COMMENTED) AS NECESSARY
BRICK_COLORS = [colormodel.RED, colormodel.ORANGE,colormodel.YELLOW, colormodel.GREEN,colormodel.CYAN]