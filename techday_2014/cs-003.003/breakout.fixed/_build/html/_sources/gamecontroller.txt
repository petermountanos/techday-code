.. CS.003: Breakout
.. Game Controller Documentation


Class GameController
====================

.. _MotionEvent: http://kivy.org/docs/api-kivy.input.motionevent.html#kivy.input.motionevent.MotionEvent

.. autoclass:: breakoutGraphics.GameController

Immutable Attributes
--------------------

These attributes may be read (e.g. used in an expression), but not altered.

.. currentmodule:: breakoutGraphics
.. autoattribute:: GameController.view

Methods
-------

Methods to Override
~~~~~~~~~~~~~~~~~~~

.. automethod:: GameController.initialize
.. automethod:: GameController.update
.. automethod:: GameController.on_touch_down
.. automethod:: GameController.on_touch_up
.. automethod:: GameController.on_touch_move

Utility Methods
~~~~~~~~~~~~~~~~
.. automethod:: GameController.delay
