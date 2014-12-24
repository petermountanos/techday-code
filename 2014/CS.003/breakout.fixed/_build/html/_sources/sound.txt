.. CS.003: Breakout
.. Sound Documentation
.. _sound-label:

Class Sound
=============

.. class:: Sound(filename)

	A sound is a WAV or OGG file that can be played on command via
	the method `play`.  When a sound is played, it cannot be played
	again until it finishes, or is stopped.  This means that if you
	want multiple, simultaneous sound effects from the same WAV
	(or OGG file), you will need to create multiple Sound objects.
	
	In order for Kivy to find a WAV or OGG file, you should put 
	it in the Sounds directory.  Sounds in that folder can
	be referenced directly by name and do not need a full 
	path name.
	
	**Constructor**: Makes a new sound instance from filename
	
		:param filename: Name of WAV or OGG file with sound
		
		**Precondition**: A string
	
	The object returned is actually of type `pygame.mixer.Sound <http://www.pygame.org/docs/ref/mixer.html>`_;
	however, you only need to import the :doc:`breakoutGraphics <graphics>` module to
	use it.

Methods
-------

These methods are documented in the class `pygame.mixer.Sound <http://www.pygame.org/docs/ref/mixer.html>`_.  We
present the most important ones here as a convenience.

.. method:: Sound.play(loops=0, maxtime=0, fade_ms=0)

	Begin playback of the Sound (i.e., on the computer's speakers) on an 
	available mixer Channel. This will forcibly select a Channel, so playback 
	may cut off a currently playing sound if necessary.

	The loops argument controls how many times the sample will be repeated 
	after being played the first time. A value of 5 means that the sound 
	will be played once, then repeated five times, and so is played a 
	total of six times. The default value (zero) means the Sound is not 
	repeated, and so is only played once. If loops is set to -1 the Sound 
	will loop indefinitely (though you can still call stop() to stop it).

	The maxtime argument can be used to stop playback after a given number 
	of milliseconds.

	The fade_ms argument will make the sound start playing at 0 volume and 
	fade up to full volume over the time given. The sample may end before 
	the fade-in is complete.

	This returns the Channel object for the channel that was selected.

.. method:: Sound.stop()

	This will stop the playback of this Sound on any active Channels.

.. method:: Sound.fadeout(time)

	This will stop playback of the sound after fading it out over the time 
	argument in milliseconds. The Sound will fade and stop on all actively 
	playing channels.

.. method:: Sound.set_volume(time)

	This will set the playback volume (loudness) for this Sound. This will 
	immediately affect the Sound if it is playing. It will also affect any 
	future playback of this Sound. The argument is a value from 0.0 to 1.0.

.. method:: Sound.get_volume()

	Return: value from 0.0 to 1.0 representing the volume for this Sound.

.. method:: Sound.get_length()

	Return: the length of this Sound in seconds.