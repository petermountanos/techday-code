.. CS.003: Breakout
.. graphicsObject Documentation

Class graphicsObject
====================

.. _Widget: http://kivy.org/docs/api-kivy.uix.widget.html

.. autoclass:: breakoutGraphics.graphicsObject

This class is a subclass of Widget_ from Kivy, and inherits
all of its attributes and methods.

Attributes
----------

.. currentmodule:: breakoutGraphics
.. autoattribute:: graphicsObject.linecolor
.. autoattribute:: graphicsObject.fillcolor

.. attribute:: graphicsObject.center

	The center position of this graphics object.

	**Invariant**: A tuple of the attributes (center_x, center_y).  
	Hence changing this attribute will change those attributes.
	The elements of the tuple must be numbers (int or float).

.. attribute:: graphicsObject.center_x

	The x coordinate of the center of this graphics object.
	
	**Invariant**: Must be equal to (x + width / 2).  Hence
	changing this attribute will change those attributes.
	The value must be a number (int or float).

.. attribute:: graphicsObject.center_y

	The y coordinate of the center of this graphics object.
	
	**Invariant**: Must be equal to (y + height / 2).  Hence
	changing this attribute will change those attributes.
	The value must be a number (int or float).
	
.. attribute:: graphicsObject.height

	The height of this graphics object.
	
	**Invariant**: Must be a non-negative number (int or float). 
	Default value is 100.

.. attribute:: graphicsObject.pos

	The position of this graphics object.

	**Invariant**: A tuple of the attributes (x, y).  
	Hence changing this attribute will change those attributes.
	The elements of the tuple must be numbers (int or float).

.. attribute:: graphicsObject.right

	The position of the right this graphics object.

	**Invariant**: Must be equal to (x + width).  Hence
	changing this attribute will change those attributes.
	The value must be a number (int or float).

.. attribute:: graphicsObject.size

	The size of this graphics object.

	**Invariant**: A tuple of the attributes (width, height).  
	Hence changing this attribute will change those attributes.
	The elements of the tuple must be numbers (int or float).

.. attribute:: graphicsObject.top

	The position of the top of this graphics object.

	**Invariant**: Must be equal to (y + height).  Hence
	changing this attribute will change those attributes.
	The value must be a number (int or float).

.. attribute:: graphicsObject.width

	The width of this graphics object.
	
	**Invariant**: Must be a non-negative number (int or float). 
	Default value is 100.

.. attribute:: graphicsObject.x

	The x position of this graphics object (specifically, the lower left corner).
	
	**Invariant**: Must be a non-negative number (int or float). 
	Default value is 0.

.. attribute:: graphicsObject.y

	The y position of this graphics object (specifically, the lower left corner).
	
	**Invariant**: Must be a non-negative number (int or float). 
	Default value is 0.

Methods
-------

These methods are all inherited from the base class Widget_ provided in Kivy.
You should use them to determine whether or not two graphics objects have
collided.

.. method:: graphicsObject.collide_point(x, y)

	Returns `True` if (x,y) is inside this graphics object; `False` otherwise.
		
		:param x: x position in the :doc:`GameView <gameview>`.

		**Precondition**: a number (int or float)

		:param y: y position in the :doc:`GameView <gameview>`.
		
		**Precondition**: a number (int or float)

	The graphics object is defined by the rectangle whose
	bottom left corner is at `pos`, and which has the the same 
	`width` and `height` as this object.  This method checks if 
	(x,y) is in this region.

.. method:: graphicsObject.collide_widget(wid)

	This method does nothing.  
	
	It has been disabled so that you implement this functionality in the way 
	specified in the assignment.