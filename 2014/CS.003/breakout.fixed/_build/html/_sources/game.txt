.. CS.003: Breakout
.. Game Classes Documentation

Game Classes
============

The game classes provide functionality for a simple animated
game.  They provide the base classes for the view and primary
controller.  The view, :doc:`GameView <gameview>`, does not ever need to be 
subclassed, and can be used as-is (as an attribute of 
:doc:`GameController <gamecontroller>`).

On the other hand, :doc:`GameController <gamecontroller>` must be subclassed to
provide your game functionality.  In particular, your
subclass must override the following methods.

        `initialize`: Called at the start of the game to initialize your
        program.  It is preferable to put start-up code here rather than
        in your constructor.
        
        `update`: Called every animation frame (60x a second). This is
        where you add any game animation code.
        
        `on_touch_down`: Called whenever the user presses the mouse or
        a finger (for a touch screen device).  

        `on_touch_up`: Called whenever the user releases the mouse or
        a finger (for a touch screen device).  Every touch_down event
        has a corresponding touch_up event.
        
        `on_touch_move`: Called whenever the user moves the mouse or
        a finger while it is still help down.  touch_move events are
        optional for each press, while touch_down and touch_up are not.

These classes are all provided by the :doc:`breakoutGraphics <graphics>` module.    

Contents:

.. toctree::
   :maxdepth: 2
   
   gameview
   gamecontroller