# controller.py
# Wantagh techDay - CS.003 Lecture 3
# Created by:    Peter Mountanos
# Modified from: Walker White (Cornell University)
# Date Created:  11/20/13
# Last Modified: 11/20/13
"""Controller module for the final project of CS.003, Breakout

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
   
    # FIELDS

    # Current play state of the game; needed by the on_touch methods
    # Invariant: One of STATE_INACTIVE, STATE_PAUSED, STATE_ACTIVE
    _state  = STATE_INACTIVE

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

    # ADD MORE FIELDS (AND THEIR INVARIANTS) AS NECESSARY
    
    # Welcome Message for the Game
    # Invariant: An object that is an instance of graphicsLabel (or a subclass)
    # Can also be None
    _message = None
    
    # Coordinates of last touch event (relative to center of paddle)
    # Invariant: Float or None.  If None, mouse/finger has been released.
    # If field is None, on_touch_move, and on_touch_up can safely do nothing
    # (valuable state information).
    _anchor = None
    
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
    _coming = None
    
    # Final Message for the Game
    # Notifies the player that they either won or lost
    # Invariant: An object that is an instance of graphicsLabel (or a subclass)
    # Also can be None depending on game state
    _finalMessage = None
    
    # Widget that displays to player how many lives they have left
    # If game state is STATE_ACTIVE or STATE_PAUSED, or STATE_COMPLETE
    # it will be displayed in the top left corner of the screen
    # Invariant: An object that is an instance of graphicsLabel (or a subclass)
    # Also can be None, depending on game state
    _lifeCounter = None
    
    # Widget that displays to player what their score is
    # If game state is STATE_ACTIVE or STATE_PAUSED, or STATE_COMPLETE
    # it will be displayed in the top right corner of the screen
    # Invariant: An object that is an instance of graphicsLabel (or a subclass)
    # Also can be None, depending on game state
    _scoreKeeper = None
    
    # Stores the current score the player has
    # When the program is  first initialized, the players score is zero
    # When the ball collides with the brick, the players score is increased
    # by 10 units.  If they lose, their score is reset back to zero,
    # if they decide to play again. However, if they win, their score is
    # carried over onto the next game.
    # Invariant: An int >= 0 
    _score = 0

    # Widget that displays to player what level they're on
    # If game state is STATE_ACTIVE or STATE_PAUSED, or STATE_COMPLETE
    # it will be displayed in the top middle of the screen
    # Invariant: An object that is an instance of graphicsLabel (or a subclass)
    # Also can be None, depending on game state
    _levelKeeper = None
    
    # Stores the current level the player is on
    # When the program is first initialized, the players level is one
    # When the player clears all the bricks from the screen, they are prompted
    # to go to the next level. If they click on the screen to continue, their
    # level is increased by 1 unit. If they lose, their level is reset to one,
    # if they choose to play again.
    # Invariant: An int >= 1
    _level = 1
    
    # Keeps count of which audio file to play when the ball hits a brick
    # This field is used to keep count for the index of BRICKS_AUDIO
    # When the program is initialized, this field is set to zero. Each
    # time the ball hits a brick, this field is increased by one. However,
    # when the field reaches the value len(BRICKS_AUDIO), it is reset to
    # zero, inturn, starting the list over to play the sounds. It prevents
    # redundancy in the noises
    # Invariant: An int >= 0 and <= len(BRICKS_AUDIO)
    _audioCounter = 0
    
    # Keeps track of if the player wants the sound to be on or off
    # If set to true, the sounds in the game will play like they are
    # normally supposed to. However, if set to false, the sounds in the
    # game will stop being played, once turned to false (will not stop
    # playing a sound if set to False in the middle of playing a sound
    # , aka it will let that sound finish, and then play no more sounds).
    # Invariant: A boolean expressions (aka True or False)
    _soundToggle = True
    
    # Image that shows the play icon on the top middle portion of the screen
    # If game state is STATE_ACTIVE or STATE_PAUSED, or STATE_COMPLETE
    # it will be displayed. If clicked, the field soundToggle will be set
    # to true. Invariant: An object that is an instance of graphicsImage
    # Also can be None, depending on game state
    _soundPlay = None
    
    # Image that shows the pause icon on the top middle portion of the screen
    # If game state is STATE_ACTIVE or STATE_PAUSED, or STATE_COMPLETE
    # it will be displayed. If clicked, the field soundToggle will be set
    # to false. Invariant: An object that is an instance of graphicsImage
    # Also can be None, depending on game state
    _soundPause = None
    
    # METHODS

    def initialize(self):
        """Initialize the game state.

        Initialize any state fields as necessary to statisfy invariants.
        When done, sets the state to STATE_INACTIVE, and displays a message
        saying that the user should press to play a game."""
        
        # Greeting Sound
        if self._level == 1:
            startoff = Sound('warpup.wav')
            startoff.play()

        self._state = STATE_INACTIVE
        self._message = graphicsLabel(text='Press to Play!',halign='center',
                               valign='middle',width=GAME_WIDTH,
                               height=GAME_HEIGHT)
        self.view.add(self._message)
        
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

        # Check to see if player won
        if self._state == STATE_ACTIVE and len(self._bricks) == 0:
            self._gameWon()
            
        elif self._state == STATE_ACTIVE and self._lives > 0:
            self._ball.updatePos()
            self._checkBounds()
            
            if not self._coming is None:
                self.view.remove(self._coming)
                self._coming = None
            
            if self._state == STATE_PAUSED:
                self._newBall()
                
            self._handleCollision()
            
        elif self._state == STATE_PAUSED:
            pass
        else:
            pass
           
    def on_touch_down(self,view,touch):
        """Respond to the mouse (or finger) being pressed (but not released)

        If state is STATE_ACTIVE or STATE_PAUSED, then this method should
        check if the user clicked inside the paddle and begin movement of the
        paddle.  Otherwise, if it is one of the other states, it moves to the
        next state as appropriate.

        Precondition: view is just the view attribute (unused because we have
        access to the view attribute).  touch is a MotionEvent (see
        documentation) with the touch information."""
        # IMPLEMENT ME
        
        if self._state == STATE_PAUSED or self._state == STATE_ACTIVE: 
            if self._paddle.collide_point(touch.x,touch.y):
                self._anchor = self._paddle.center_x - touch.x
                
            if self._soundPlay.collide_point(touch.x,touch.y):
                self._soundToggle = True
            elif self._soundPause.collide_point(touch.x,touch.y):
                self._soundToggle = False
        
        if self._state == STATE_INACTIVE:
            self.view.remove(self._message)    
            self._state = STATE_PAUSED
            
            # Add Widgets
            self._addTopBar()    

            # Add Bricks
            self._brickSetup()
            
            # Add Paddle
            self._paddle = graphicsRectangle(pos=(GAME_WIDTH/2-PADDLE_WIDTH/2,
                                           PADDLE_OFFSET),size=(PADDLE_WIDTH,
                                                                PADDLE_HEIGHT)) 
            self.view.add(self._paddle)
            
            # Add Ball
            self._ball = Ball()
            self.delay(self._serveBall,3) # three second delay
        
        if self._state == STATE_COMPLETE:
            self.view.remove(self._paddle)
            self.view.remove(self._ball)
            self.view.remove(self._finalMessage)
            self.view.remove(self._lifeCounter)
            self.view.remove(self._scoreKeeper)
            self.view.remove(self._levelKeeper)
            self.view.remove(self._soundPlay)
            self.view.remove(self._soundPause)
            for i in range(len(self._bricks)):
                self.view.remove(self._bricks[i])
            self._lives = 3
            self._bricks = []
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
        # IMPLEMENT ME

        if ((self._state == STATE_ACTIVE or self._state == STATE_PAUSED)
            and (not self._anchor is None)):
            self._paddle.center_x = self._paddle.center_x - self._anchor 
            self._keepInBounds()
            self._anchor = self._paddle.center_x - touch.x # stores previous movement
        else:
            pass

    def on_touch_up(self,view,touch):
        """Respond to the mouse (or finger) being released.

        If state is STATE_ACTIVE, then this method should stop moving the
        paddle. For all other states, it is ignored.

        Precondition: view is just the view attribute (unused because we have
        access to the view attribute).  touch is a MotionEvent (see
        documentation) with the touch information."""
        # IMPLEMENT ME
        
        if self._state == STATE_ACTIVE:
            self._anchor = None
        else:
            pass
        
    # ADD MORE HELPER METHODS (PROPERLY SPECIFIED) AS NECESSARY
    
    def _serveBall(self):
        """Function to call when a new ball needs to be added.
        Adds an instance of Ball to the view."""
        
        self.view.add(self._ball)
        self._state = STATE_ACTIVE
    
    def _brickSetup(self):
        """Helper Method for setting up the bricks.
        
        The number, dimensions, and spacing of the bricks, as well as the
        distance from the top of the window to the first line of bricks, are
        colors of the bricks remain constant for two rows and run in the
        following sequence: RED,ORANGE,YELLOW,GREEN,CYAN. If there are more
        than ten rows, it starts over with RED, and does the sequence again.
        Also creates a paddle after setting up the bricks."""

        for x in range(BRICK_ROWS):
            # Determines how to space and place rows
            distance_y = ((GAME_HEIGHT - BRICK_Y_OFFSET) - (x * BRICK_HEIGHT) -
                (BRICK_SEP_V * x))
            # Sets color for row
            if x % 10 == 0 or x % 10 == 1:
                bcolor = BRICK_COLORS[0]
            elif x % 10 == 2 or x % 10 == 3:
                bcolor = BRICK_COLORS[1]
            elif x % 10 == 4 or x % 10 == 5:
                bcolor = BRICK_COLORS[2]
            elif x % 10 == 6 or x % 10 == 7:
                bcolor = BRICK_COLORS[3]
            else:
                bcolor = BRICK_COLORS[4]
                
            for i in range(BRICKS_IN_ROW):
                # Determines how to space and place bricks in row
                distance_x = (BRICK_SEP_H/2.0 + (i * BRICK_WIDTH) +
                              (BRICK_SEP_H * i))
                brick = graphicsRectangle(pos=(distance_x,distance_y),
                                    size=(BRICK_WIDTH,BRICK_HEIGHT),
                                    fillcolor=bcolor,linecolor=bcolor) 
                self.view.add(brick) # add to view
                self._bricks.append(brick) # add to controller
        
    def _getCollidingraphicsObject(self):
        """Returns: graphicsObject that has collided with the ball=
        
        This method checks the four corners of the ball, one at a
        time. If one of these points collides with either the paddle
        or a brick, it stops the checking immediately and returns the
        objects involved in the collision. It returns None if no
        collision occurred."""
        
        top_left = (self._ball.x, self._ball.y + BALL_DIAMETER)
        top_right = (self._ball.x + BALL_DIAMETER, self._ball.y + BALL_DIAMETER)
        bottom_left = (self._ball.x, self._ball.y)
        bottom_right = (self._ball.x + BALL_DIAMETER, self._ball.y)
        corners = [top_left,top_right,bottom_left,bottom_right]
        
        for c in range(len(corners)):

            # Checks each brick for all four corners
            for i in range(len(self._bricks)):
                if self._bricks[i].collide_point(corners[c][0],corners[c][1]):
                    return self._bricks[i]
                
            # Checks paddle for all four corners   
            if self._paddle.collide_point(corners[c][0],corners[c][1]):
                    return self._paddle
            
        return None # no collision occured
    
    def _checkBounds(self):
        """Checks the boundaries of the playing field.
        
        If the ball hits the bottom wall, the player loses a
        life.  If the ball hits any of the three other walls
        its respective component of its velocity is negated."""
        
        if self._ball.y <= 0:
            self._loseLife()
        elif self._ball.top >= GAME_HEIGHT:
            self._ball.vy = - self._ball.vy
        elif self._ball.x <= 0 or self._ball.right >= GAME_WIDTH:
            self._ball.vx = - self._ball.vx
    
    def _loseLife(self):
        """Function is called when the ball hits the bottom wall.
        
        The player begins with three lives, and when the ball hits
        the bottom wall, the player loses a life. """
        
        self._lives = self._lives - 1
        self._state = STATE_PAUSED
        self._lifeCounter.text = 'Lives Remaining: '+`self._lives`
        
        if self._lives == 0:
            return self._gameOver()
            
        self.view.remove(self._ball)
        self._ball = None
    
    def _gameOver(self):
        """Function is called when the player's lives hits zero.
        
        This function removes the warning message, and adds an
        admonishing message. Finally,it sets the state of the game
        to the constant STATE_COMPLETE. Also resets the score to
        zero and plays the game over sound."""
        
        self._finalMessage = graphicsLabel(text='Sorry You Lost\n You ran out of lives'
                                    +'\n\nClick on the Screen to Play Again\nor'
                                    +' Close to Exit',halign='center',
                                    valign='middle',width=GAME_WIDTH,
                                    height=GAME_HEIGHT - BRICK_Y_OFFSET/2)
        self.view.add(self._finalMessage)
        self._score = 0
        if self._soundToggle:
            warpDown = Sound('warpdown.wav')
            warpDown.play()
        self._state = STATE_COMPLETE
    
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
        
        collision = self._getCollidingraphicsObject() # Checks for Collisions 
   
        if collision == self._paddle and self._ball.vy > 0:
            pass # nothing happens when the ball is going up and hits the paddle
        elif collision == self._paddle and self._ball.vy < 0:
            if self._soundToggle:
                paddleSound = Sound('bounce.wav')
                paddleSound.play()
            self._ball.vy = - self._ball.vy # change direction
        elif collision in self._bricks:
            if self._soundToggle:
                brickNoise = Sound(BRICKS_AUDIO[self._audioCounter])
                brickNoise.play()
                self._audioCounter = self._audioCounter + 1
                if self._audioCounter == len(BRICKS_AUDIO):
                    self._audioCounter = 0
            self._ball.vy = - self._ball.vy # change direction
            self.view.remove(collision) # remove from view
            self._bricks.remove(collision) # remove from field
            self._score = self._score + 10
            self._scoreKeeper.text = 'Current Score : '+`self._score`
        
    def _keepInBounds(self):
        """This method keeps the paddle within the boundaries of the window.
        
        Although short, this helper method is mainly for styling purposes.
        It allows for easier readibility within the function its placed.
        If the player slides the mouse/touches outside the width of the game
        screen, the paddle is essentially "locked" to the respective edge the
        mouse/finger went off of."""
        
        if self._paddle.center_x-29 <= 0:
            self._paddle.center_x = 30
        elif self._paddle.center_x+29 > 480:
            self._paddle.center_x = 450
    
    def _gameWon(self):
        """This method is called when the player has won the game!
        (i.e. all of the bricks have been removed from the screen)
        
        All this method does is add a congratulator message and sets
        the game state to STATE_COMPLETE. Also increases the level by one
        Again, mainly for readibility and styling purposes."""
        
        self._finalMessage = graphicsLabel(text='You beat this level!\n\nClick on the'
                                    +' screen to commence to the next level\nor'
                                    +' close to exit'
                                    ,halign='center',valign='middle',
                                    width=GAME_WIDTH,height=(GAME_HEIGHT -
                                                             BRICK_Y_OFFSET/2))
        self.view.add(self._finalMessage)
        self._level = self._level + 1
        self._levelKeeper.text = 'Level '+`self._level`
        self._state = STATE_COMPLETE
    
    def _newBall(self):
        """If state is paused while it was already active, and the player
        still has lives left, a new ball must be served.
        
        This method creates a warning message that a new ball is coming,
        and that the player should re-center their paddle to prepare for
        the ball.  It then adds a new ball, with a three second delay, to
        allow the user to have enough time to reset their paddle position
        and prepare for the upcoming life."""
        
        if self._soundToggle:
            tickTock = Sound('ticktock.wav')
            tickTock.play()
            
        self._coming = graphicsLabel(text='Ball is Coming!!!!!!',halign='center',
                                 valign='middle',width=GAME_WIDTH,
                                 height=GAME_HEIGHT)
        self.view.add(self._coming)
        
        self._ball = Ball()
        self.delay(self._serveBall,3) # three second delay
    
    def _addTopBar(self):
        """Adds widgets to the top portion of the screen above the bricks.
        
        If self._state is STATE_ACTIVE when on_touch_down is called, this
        method is called. It sets all of the widgets (life counter, score
        keeper, sound play and sound play, and level keeper) to their appro-
        priate values, and then adds them to the view."""
        
        self._lifeCounter = graphicsLabel(text='Lives Remaining : '+`self._lives`,
                                halign='left',valign='top',
                                width=GAME_WIDTH,height=GAME_HEIGHT,
                                       x=20)
        self._scoreKeeper = graphicsLabel(text='Current Score : '+`self._score`,
                            halign='right',valign='top',
                           width=GAME_WIDTH-20,height=GAME_HEIGHT)
        self._levelKeeper = graphicsLabel(text='Level '+`self._level`,
                                   halign='center',valign='top',
                               width=GAME_WIDTH,height=GAME_HEIGHT)
            
        self._soundPlay = graphicsImage(imageSource='play.png',
                        size=(25,25),
                        pos=((GAME_WIDTH/2.0)-26,GAME_HEIGHT-55))
        self._soundPause = graphicsImage(imageSource='pause.png',
                        size=(25,25),
                        pos=((GAME_WIDTH/2.0)+1,GAME_HEIGHT-55))
        
        self.view.add(self._soundPlay)
        self.view.add(self._soundPause)    
        self.view.add(self._lifeCounter)
        self.view.add(self._scoreKeeper)
        self.view.add(self._levelKeeper)
        
        
class Ball(graphicsImage):
    """Instance is a game ball.

    It extends graphicsImage because a ball does not just have a position; it
    also has a velocity.  You should add a constructor to initialize the
    ball, as well as one to move it.  It also can now handle images.

    Note: The ball does not have to be a graphicsEllipse. It could be an instance
    of graphicsImage (why?). This change is allowed, but you must modify the class
    header up above."""
    # FIELDS.  You may wish to add properties for them, but that is optional.

    # Velocity in x direction.  A number (int or float)
    _vx = 0.0
    # Velocity in y direction.  A number (int or float)
    _vy = 0.0

    # ADD MORE FIELDS (INCLUDE INVARIANTS) AS NECESSARY
    
    # PROPERTIES
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

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    
    # Constructor
    def __init__(self):
        """Constructor: Creates a new Ball.
        
        The vx and vy values not arguments. For vy, it is already
        determined to start as -5.0. For vx, a random number is generated
        to represent the speed.
        
        The ball's initial starting position, size, and background image
        are called with super, as those attributes come from the superclasses
        of both graphicsImage and graphicsObject."""
        
        super(Ball,self).__init__(pos=(GAME_WIDTH/2-BALL_DIAMETER/2,
                                       GAME_HEIGHT/2+BALL_DIAMETER/2),
                                  size=(BALL_DIAMETER,BALL_DIAMETER)
                                  ,imageSource='beach-ball.png')
        
        self.vx = random.uniform(1.0,5.0)
        self.vx = self._vx * random.choice([-1,1])
        self.vy = -5.0
    
    def updatePos(self):
        """Helps move the ball one step at a time.
        
        This is accomplished by adding the ball's velocity
        components to the ball's corresponding position coordinates.
        This function is not hidden, because Breakout must be able to
        "see" this function in order to call it."""
        
        self.x = self.x + self.vx
        self.y = self.y + self.vy

# ADD MORE CLASSES AS NECESSARY
