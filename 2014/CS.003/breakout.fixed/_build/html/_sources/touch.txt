.. CS:003 Breakout
.. Touch Documentation

Class MotionEvent
=================

.. _MotionEvent: http://kivy.org/docs/api-kivy.input.motionevent.html#kivy.input.motionevent.MotionEvent

A `MotionEvent`_ is a class provided by Kivy.  You will never construct a
Motion event but you will recieve them as the touch values for the :doc:`on_touch <gamecontroller>`
methods in :doc:`GameController <gamecontroller>`.

.. class:: MotionEvent

	Objects of this class represent touch events in Kivy.

Immutable Attributes
--------------------

The attributes of this class are detailed in full at the Kivy `MotionEvent`_ 
documention.  We present the most important attributes here.  

All of these attributes are essentially *immutable*.  You should not attempt 
to change them.  The purpose of a `MotionEvent`_ is to get information about a 
touch event.  If you change these values, you are changing the nature of
the touch event.

.. attribute:: x

	The x position of this touch.

	**Invariant**: A number (int or float) 

.. attribute:: y

	The y position of this touch.

	**Invariant**: A number (int or float) 

.. attribute:: is_double_tap

	`True` if the touch is a double tap; `False` otherwise

	**Invariant**: A bool

.. attribute:: double_tap_time

	If the touch is a is_double_tap, this is the time between the 
	previous tap and the current touch.

	**Invariant**: A positive number (int or float), or `None` 
	if touch is not a double tap.

.. attribute:: time_end

	Time of the end event (last touch usage)

	**Invariant**: A positive number (int or float), or `None` 
	if this is the first usage of touch.

.. attribute:: time_start

	Initial time of the touch creation

	**Invariant**: A positive number (int or float).

.. attribute:: time_update

	Initial time of the last update (e.g. touch movement)
	
	**Invariant**: A positive number (int or float).


Methods
-------

The methods of this class are detailed in full at the Kivy `MotionEvent`_ 
documention.  However, you should *not* need to use any methods.  Only
the attributes mentioned are important for this project.