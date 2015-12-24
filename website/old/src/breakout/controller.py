# controller.py
# Wantagh techDay - CS.003 Lecture 3
# Created by:    Peter Mountanos
# Modified from: Walker White (Cornell University)
# Date Created:  11/20/13
# Last Modified: 11/20/13
"""Controller module for the practical application of CS.003, Breakout

This module contains a class for the game Breakout.
Unlike the other files in this project, you are 100% free to change
anything in this file. You can add and/or remove classes."""

# Importing necessary libraries
import colormodel
import random
from breakoutGraphics import *
from constants import *

# CLASSES
class Breakout(GameController):
    """Instance is the primary controller for Breakout.

    This class extends GameController and implements the various methods
    necessary for running the game.

        Method   : initialize : starts up the game

        Method   :   update   : animates the ball and provides the physics

        Methods  :  on_touch  : handle mouse (or finger) input

    The class also has fields that provide state to this controller.
    The fields can all be hidden; you do not need properties. However,
    you should clearly state the field invariants, as the various
    methods will rely on them to determine game state."""
   
    #---------------------------------------------------------------#
    #----------------------------FIELDS-----------------------------#
    #---------------------------------------------------------------#

    # Current play state of the game; needed by the on_touch methods
    # Invariant: One of STATE_INACTIVE, STATE_PAUSED, STATE_ACTIVE
    _state  = STATE_INACTIVE

    # Coordinates of last touch event (relative to center of paddle)
    # Invariant: Float or None.  If None, mouse/finger has been released.
    # If field is None, on_touch_move, and on_touch_up can safely do nothing
    # (valuable state information).
    _anchor = None

    # List of currently active "bricks" in the game.
    # Invariant: A list of  objects that are instances of graphicsRectangle (or a
    # subclass) If list is  empty, then state is STATE_INACTIVE (or game over)
    _bricks = []

    # The player paddle
    # Invariant: An object that is an instance of graphicsRectangle (or a subclass)
    # Also can be None; if None, then state is STATE_INACTIVE (game over)
    _paddle = None
    
    # The ball to bounce about the game board
    # Invariant: An object that is an instance of graphicsEllipse (or a subclass)
    # Also can be None; if None, then state is STATE_INACTIVE (game over) or
    # STATE_PAUSED (waiting for next ball)
    _ball = None
    
    # Welcome Message for the Game
    # Invariant: An object that is an instance of graphicsLabel (or a subclass)
    # Can also be None
    _welcomeLabel = None

    # Stores the amount of lives the player has
    # Invariant: must be an int in the range 0-3. In a single game, the
    # player starts with 3 lives, and when the ball hits the bottom level
    # they lose a life. When the amount of lives hits zero, the game is
    # over and the state changes to STATE_COMPLETE
    _lives = 3

    # Warning Message for the Game
    # Warns a player that another ball is coming
    # Invariant: An object that is an instance of graphicsLabel (or a subclass)
    # Also can be None depeneding on game state
    _ballWarning = None
    
    # Final Message for the Game
    # Notifies the player that they either won or lost
    # Invariant: An object that is an instance of graphicsLabel (or a subclass)
    # Also can be None depending on game state
    _finalMessage = None
    
    #---------------------------------------------------------------#
    #----------------------------METHODS----------------------------#
    #---------------------------------------------------------------#

    def initialize(self):
        """Initialize the game state.

        Initialize any state fields as necessary to statisfy invariants.
        When done, sets the state to STATE_INACTIVE, and displays a message
        saying that the user should press to play a game."""
        
        # Create Welcome Label
        self._welcomeLabel = graphicsLabel(text='Press to Play!', halign='center',
                            valign='middle',width=GAME_WIDTH, height=GAME_HEIGHT)
        # Add Welcome Label to view
        self.view.add(self._welcomeLabel)
        # State Game State to Inactive (waiting for ball)
        self._state = STATE_INACTIVE
        
    def update(self, dt):
        """Animate a single frame in the game.

        This is the method that does most of the work.  It moves the ball, and
        looks for any collisions.  If there is a collision, it changes the
        velocity of the ball and removes any bricks if necessary.

        This method may need to change the state of the game.  If the ball
        goes off the screen, change the state to either STATE_PAUSED (if the
        player still has some tries left) or STATE_COMPLETE (the player has
        lost the game).  If the last brick is removed, it needs to change
        to STATE_COMPLETE (game over; the player has won).

        Precondition: dt is the time since last update (a float).  This
        parameter can be safely ignored."""

        # If ball is in play...
        if self._state == STATE_ACTIVE:
            # Update ball position
            self._ball.updatePos()
            # Check ball boundaries
            self._checkBallBounds()
            # If the ball warning message is on the screen...
            if not self._ballWarning is None:
                # Remove ball warning message
                self.view.remove(self._ballWarning)
                # Set the ball warning message field to none
                self._ballWarning = None
            # If a life is lost (ball hits the bottom)
            if self._state == STATE_PAUSED:
                # Serve a new ball
                self._newBall()
            # Constantly handle any potential collisions
            self._handleCollision()

    def on_touch_down(self,view,touch):
        """Respond to the mouse (or finger) being pressed (but not released)

        If state is STATE_ACTIVE or STATE_PAUSED, then this method should
        check if the user clicked inside the paddle and begin movement of the
        paddle.  Otherwise, if it is one of the other states, it moves to the
        next state as appropriate.

        Precondition: view is just the view attribute (unused because we have
        access to the view attribute).  touch is a MotionEvent (see
        documentation) with the touch information."""
    
        if self._state == STATE_INACTIVE: # if game just started
            # set state to inbetween state which represents the 
            # time when the user turns on the game, and when they
            # are waiting for the ball
            self._state = STATE_PAUSED
            # removes welcome label from the screen of view
            self.view.remove(self._welcomeLabel)
            # call helper function to set up bricks 
            self._setUpBricks()
            # add the paddle to the view
            self._paddle = graphicsRectangle(fillcolor=colormodel.BLACK,
                           linecolor=colormodel.BLACK, pos=(GAME_WIDTH/2 - PADDLE_WIDTH/2,PADDLE_OFFSET),
                           size=(PADDLE_WIDTH,PADDLE_HEIGHT))
            self.view.add(self._paddle)

            self.delay(self._serveBall,3) # callback function to delay serve

        # if waiting for ball, or ball is in play
        elif self._state == STATE_PAUSED or self._state == STATE_ACTIVE: 
            # if the user clicks on the paddle
            if self._paddle.collide_point(touch.x,touch.y):
                self._anchor = self._paddle.center_x - touch.x
                # set anchor point (don't worry about this)
        # if the game is over (lost or won) and restarted (by pressing down)...
        elif self._state == STATE_COMPLETE:
            # remove paddle from the view
            self.view.remove(self._paddle)
            # remove ball from the view
            self.view.remove(self._ball)
            # remove winning message from view
            self.view.remove(self._finalMessage)
            # for each brick...
            for i in range(len(self._bricks)):
                # remove brick <i> from the view
                self.view.remove(self._bricks[i])
            # reset the number of lives
            self._lives = 3
            # clear bricks from array
            self._bricks = []
            # reintialize game
            self.initialize()

    def on_touch_move(self,view,touch):
        """Respond to the mouse (or finger) being moved.

        If state is STATE_ACTIVE or STATE_PAUSED, then this method should move
        the paddle. The distance moved should be the distance between the
        previous touch event and the current touch event. For all other
        states, this method is ignored.

        Precondition: view is just the view attribute (unused because we have
        access to the view attribute).  touch is a MotionEvent (see
        documentation) with the touch information."""
        
        # if user is waiting for the ball, or the ball is in play...
        # and there is a previous anchor point
        if ((self._state == STATE_ACTIVE or self._state == STATE_PAUSED) 
            and (not self._anchor is None)):
            # move paddle to new location
            self._paddle.center_x = self._paddle.center_x - self._anchor 
            # helper method to make sure paddle doesn't go off the sides of the screen
            self._keepPaddleInBounds() # to be implemented!
            # stores previous touch movement as anchor
            self._anchor = self._paddle.center_x - touch.x 
        # if ball isn't coming or being played...
        else:
            pass # don't let the paddle move around

    def on_touch_up(self,view,touch):
        """Respond to the mouse (or finger) being released.

        If state is STATE_ACTIVE, then this method should stop moving the
        paddle. For all other states, it is ignored.

        Precondition: view is just the view attribute (unused because we have
        access to the view attribute).  touch is a MotionEvent (see
        documentation) with the touch information."""
    
        # if the ball is in play
        if self._state == STATE_ACTIVE:
            self._anchor = None # clear anchor point (stops paddle movement)
        else:
            pass # this function is only needed when the ball is in play

    def _handleCollision(self):
        """This method handles what happens when a collision between
        the ball, and something other than the walls occurs.
        
        First, this method calls another hidden method _getCollidingraphicsObject(),
        and stores it in a variable called collision.  That method detects
        collisions, and if a collision does occur this method will do something,
        if not it will simply have just called the _getCollidingraphicsObject() method.
        If a collision occurs with the ball and the paddle, when the ball has a
        negative velocity, the ball's y component of the velocity is negated. If
        there is a collision with the ball and paddle, but the ball is going up,
        nothing happens. If there is a collision between the ball and a brick,
        the brick is removed, and the ball's y component of the velocity is
        negated. Also plays a specific sound depending on what object the ball
        hits."""
        
        collision = self._getCollidingObject() # Checks for Collisions 
   
        if collision == self._paddle and self._ball.vy > 0:
            pass # nothing happens when the ball is going up and hits the paddle
        # if there's a collision between the ball and paddle, and the balls going down
        elif collision == self._paddle and self._ball.vy < 0:
            self._ball.vy = - self._ball.vy # change direction of ball
        # if there's a collision between the ball and a brick
        elif collision in self._bricks:
            self._ball.vy = - self._ball.vy # change direction
            self.view.remove(collision) # remove brick from view
            self._bricks.remove(collision) # remove brick from array

    def _loseLife(self):
        """Function is called when the ball hits the bottom wall.
        
        The player begins with three lives, and when the ball hits
        the bottom wall, the player loses a life. """
        
        self._lives -= 1 # subtract one life
        self._state = STATE_PAUSED # set state to paused (waiting for ball)

        if self._lives == 0: # if the player has no more lives left
            return self._gameOver() # call the helper function game over
            
        self.view.remove(self._ball) # remove the ball object from the screen
        self._ball = None # set the ball to none

    def _newBall(self):
        """If state is paused while it was already active, and the player
        still has lives left, a new ball must be served.
        
        This method creates a warning message that a new ball is coming,
        and that the player should re-center their paddle to prepare for
        the ball.  It then adds a new ball, with a three second delay, to
        allow the user to have enough time to reset their paddle position
        and prepare for the upcoming life."""
        # set warning message
        self._ballWarning = graphicsLabel(text='The ball is coming!',halign='center',
                                 valign='middle',width=GAME_WIDTH,
                                 height=GAME_HEIGHT)
        self.view.add(self._ballWarning) # add message to view
        
        self._ball = Ball() # create new Ball object
        self.delay(self._serveBall,3) # three second delay before serve

    def _gameOver(self):
        """Function is called when the player's lives hits zero.
        
        This function removes the warning message, and adds an
        admonishing message. Finally,it sets the state of the game
        to the constant STATE_COMPLETE. Also resets the score to
        zero and plays the game over sound."""
        
        # set admonishing message
        self._finalMessage = graphicsLabel(text='Sorry You Lost\n You ran out of lives'
                                    #+'\n\nClick on the Screen to Play Again\nor'
                                    #+' Close to Exit'
                                    ,halign='center',
                                    valign='middle',width=GAME_WIDTH,
                                    height=GAME_HEIGHT - BRICK_Y_OFFSET/2)
        # add losing message to view
        self.view.add(self._finalMessage)
        self._state = STATE_COMPLETE # set state to complete (game over)

    def _gameWon(self):
        """This method is called when the player has won the game!
        (i.e. all of the bricks have been removed from the screen)
        
        All this method does is add a congratulator message and sets
        the game state to STATE_COMPLETE. Also increases the level by one
        Again, mainly for readibility and styling purposes."""
    
        # set winning message
        self._finalMessage = graphicsLabel(text='Congratulations, you won!'+
                                            '\nClick to play again!'
                                    ,halign='center',valign='middle',
                                    width=GAME_WIDTH,height=(GAME_HEIGHT -
                                                             BRICK_Y_OFFSET/2))
        self.view.add(self._finalMessage) # add winning message to view
        self._state = STATE_COMPLETE # set state to complete (game over)

    def _setUpBricks(self):
        """Helper Method for setting up the bricks.
        
        The number, dimensions, and spacing of the bricks, as well as the
        distance from the top of the window to the first line of bricks, are
        colors of the bricks remain constant for two rows and run in the
        following sequence: RED,ORANGE,YELLOW,GREEN,CYAN. If there are more
        than ten rows, it starts over with RED, and does the sequence again.
        Also creates a paddle after setting up the bricks."""

        # for number of brick rows
        for x in range(BRICK_ROWS):
            # compute vertical distance between bricks
            y_Distance = ((GAME_HEIGHT - BRICK_Y_OFFSET) - (x * BRICK_HEIGHT) -
                (BRICK_SEP_V * x))
            # determine brick color for the current row
            brickColor = self._findBrickColor(x)
            # for number of bricks in a row
            for i in range(BRICKS_IN_ROW):
                # compute horizontal distance between bricks in a row
                x_Distance = (BRICK_SEP_H/2.0 + (i * BRICK_WIDTH) +
                              (BRICK_SEP_H * i))
                # create brick object
                brick = graphicsRectangle(pos=(x_Distance,y_Distance),
                                    size=(BRICK_WIDTH,BRICK_HEIGHT),
                                    fillcolor=brickColor,linecolor=brickColor) 
                # add brick to view
                self.view.add(brick)
                # add brick to bricks array 
                self._bricks.append(brick)

    def _serveBall(self):
        """Function to call when a new ball needs to be added.
        Adds an instance of Ball to the view."""

        self._ball = Ball() # initializes ball object
        self.view.add(self._ball) # adds ball to the view
        self._state = STATE_ACTIVE # sets the state to active (ball in play)

#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
#----------------ONLY IMPLEMENT METHODS BELOW THIS WITHIN CLASS <BREAKOUT>----------------#
#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#

    def _checkBallBounds(self):
        """Checks the boundaries of the playing field.
        
        If the ball hits the bottom wall, the player loses a
        life.  If the ball hits any of the three other walls
        its respective component of its velocity is negated.

        First, we will implement this function that if the ball
        hits the bottom wall, negate its vertical velocity comp-
        onent (i.e., we're going to let the ball bounce around."""

        #----------------PUT CODE IN BETWEEN THESE LINES----------------#
        # method to be implemented by students
        # delete <pass> before you start your code

        if self._ball.x <= 0 or self._ball.right >= GAME_WIDTH:
            self._ball.vx *= -1

        if self._ball.top >= GAME_HEIGHT:
            self._ball.vy *= -1

        if self._ball.y <= 0:
            #self._ball.vy = - self._ball.vy 
            self._loseLife()
        #---------------------------------------------------------------#

    def _keepPaddleInBounds(self):
        """This method keeps the paddle within the boundaries of the window.
        
        Although short, this helper method is mainly for styling purposes.
        It allows for easier readibility within the function its placed.
        If the player slides the mouse/touches outside the width of the game
        screen, the paddle is essentially "locked" to the respective edge the
        mouse/finger went off of."""

        #----------------PUT CODE IN BETWEEN THESE LINES----------------#
        # method to be implemented by students
        # delete <pass> before you start your code
        if self._paddle.x <= 0:
            self._paddle.x = 0
        if self._paddle.right >= GAME_WIDTH:
            self._paddle.right = GAME_WIDTH
        #---------------------------------------------------------------#

    def _findBrickColor(self,rowNum):
        """This helper method determines the color of the brick to be
        displayed on the screen by method setUpBricks.

            :param rowNum: the current row of bricks that is being generated
            **Precondition**: Must be an integer, <= BRICK_ROWS

        This method should generate the colors of the bricks so they remain
        constant for two rows and run in the following sequence: RED,ORANGE,
        YELLOW,GREEN,CYAN. If there are more than ten rows, it starts over
        with RED, and does the sequence again."""

        #----------------PUT CODE IN BETWEEN THESE LINES----------------#
        # method to be implemented by students
        #delete <return colormodel.BLACK> before you start your code
        if rowNum % 10 == 0 or rowNum % 10 == 1:
            brickColor = BRICK_COLORS[0]
        elif rowNum % 10 == 2 or rowNum % 10 == 3:
            brickColor = BRICK_COLORS[1]
        elif rowNum % 10 == 4 or rowNum % 10 == 5:
            brickColor = BRICK_COLORS[2]
        elif rowNum % 10 == 6 or rowNum % 10 == 7:
            brickColor = BRICK_COLORS[3]
        elif rowNum % 10 == 8 or rowNum % 10 == 9:
            brickColor = BRICK_COLORS[4]

        return brickColor
        #---------------------------------------------------------------#

    def _getCollidingObject(self):
        """Returns: graphicsObject that has collided with the ball

        This method checks the four corners of the ball, one at a time. 
        If one of these points collides with either the paddle, or a brick, 
        it stops the checking immediately and returns the object involved in 
        the collision. It returns None if no collision occurred."""

        #----------------PUT CODE IN BETWEEN THESE LINES----------------#
        # method to be implemented by students
        # delete <return None> before you start your code
        # store the corners of the ball
        topLeft = (self._ball.x,self._ball.y + BALL_DIAMETER)
        topRight = (self._ball.x + BALL_DIAMETER, self._ball.y + BALL_DIAMETER)
        bottomLeft = (self._ball.x,self._ball.y)
        bottomRight = (self._ball.x + BALL_DIAMETER, self._ball.y)
        # make a list of those points
        corners = [topLeft,topRight,bottomLeft,bottomRight]
        # for loop checking each corner
        for x in range(len(corners)):

            # if touching paddle:
            if self._paddle.collide_point(corners[x][0],corners[x][1]):
                return self._paddle
                # return paddle
            # for loop checking each brick
            for i in range(len(self._bricks)):
                if self._bricks[i].collide_point(corners[x][0],corners[x][1]):
                    return self._bricks[i]
                # if touch bricks[i]
                    # return brick[i]
        return None
        # return none
        #---------------------------------------------------------------#

#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
#-----------DO NOT IMPLEMENT ANY METHODS BELOW THIS LINE WITHIN CLASS <BREAKOUT>----------#
#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#

class Ball(graphicsImage):
    """Instance is a game ball.

    It extends graphicsImage because a ball does not just have a position; it
    also has a velocity.  You should add a constructor to initialize the
    ball, as well as one to move it.  It also can now handle images.

    Note: The ball does not have to be a graphicsEllipse. It could be an instance
    of graphicsImage (why?). This change is allowed, but you must modify the class
    header up above."""

    #---------------------------------------------------------------#
    #----------------------------FIELDS-----------------------------#
    #---------------------------------------------------------------#

    # Velocity in x direction.  A number (int or float)
    _vx = 0.0
    # Velocity in y direction.  A number (int or float)
    _vy = 0.0
    
    #---------------------------------------------------------------#
    #--------------------------PROPERTIES---------------------------#
    #---------------------------------------------------------------#

    @property
    def vx(self):
        """Velocity in x direction. A number (int or float)."""
        return self._vx
    
    @vx.setter
    def vx(self, value):
        assert (type(value) == float or type(value) == int)
        self._vx = value
    
    @property
    def vy(self):
        """Velocity in y direction. A number (int or float)."""
        return self._vy
    
    @vy.setter
    def vy(self, value):
        assert (type(value) == float or type(value) == int)
        self._vy = value
    
    #---------------------------------------------------------------#
    #----------------------------METHODS----------------------------#
    #---------------------------------------------------------------#

    def __init__(self):
        """Constructor: Creates a new Ball.
        
        The vx and vy values not arguments. For vy, it is already
        determined to start as -5.0. For vx, a random number is generated
        to represent the speed.
        
        The ball's initial starting position, size, and background image
        are called with super, as those attributes come from the superclasses
        of both graphicsImage and graphicsObject."""
        
        # IMPLEMENT ME
        # subclassing graphicsImage...
        # position: middle, size: predetermined, source: beach ball image
        super(Ball,self).__init__(pos=(GAME_WIDTH/2-BALL_DIAMETER/2,
                                       GAME_HEIGHT/2+BALL_DIAMETER/2),
                                  size=(BALL_DIAMETER,BALL_DIAMETER)
                                  ,imageSource='beach-ball.png')
        # random float in range 1.0..5.0 (inclusive)
        self.vx = random.uniform(1.0,5.0)
        # will make vx negative about 1/2 the time (makes game harder)
        self.vx = self._vx * random.choice([-1,1])
        # need a downward velocity of -5.0 to begin 
        self.vy = -5.0

#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
#------------------ONLY IMPLEMENT METHODS BELOW THIS WITHIN CLASS <BALL>------------------#
#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#

    def updatePos(self):
        """Helps move the ball one step at a time.
        
        This is accomplished by adding the ball's velocity
        components to the ball's corresponding position coordinates.
        This function is not hidden, because Breakout must be able to
        "see" this function in order to call it."""

        #----------------PUT CODE IN BETWEEN THESE LINES----------------#
        # method to be implemented by students
        # delete <pass> before you start your code
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        #---------------------------------------------------------------#

#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
#-------------DO NOT IMPLEMENT ANY METHODS BELOW THIS LINE WITHIN CLASS <BALL>------------#
#-----------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------#
