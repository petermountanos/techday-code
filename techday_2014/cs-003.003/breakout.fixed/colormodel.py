# breakoutGraphics.py
# Wantagh techDay - CS.003 Lecture 3
# Created by:   Peter Mountanos
# Modified from: Walker White (Cornell University)
# Date Created:  11/19/13
# Last Modified: 11/20/13

"""RGB class for Breakout, the project for Wantagh techDay, class CS.003

The constants in this module are all defined in the RGB color space."""
import colorsys

# To handle round off error
_epsilon = 1e-13

class RGB(object):
    """An instance is an RGB color value."""
    
    @property
    def red(self):
        """The red channel.
        
        **Invariant**: value must be an int between 0 and 255, inclusive."""
        return self._red
       
    @red.setter
    def red(self, value):
        assert (type(value) == int), "value %s is not an int" % `value`
        assert (value >= 0 and value <= 255), "value %s is outside of range [0,255]" % `value`
        self._red = value
       
    @red.deleter
    def red(self):
        del self._red 
    
    @property
    def green(self):
        """The green channel.
        
        **Invariant**: value must be an int between 0 and 255, inclusive."""
        return self._green
    
    @green.setter
    def green(self, value):
        assert (type(value) == int), "value %s is not an int" % `value`
        assert (value >= 0 and value <= 255), "value %s is outside of range [0,255]" % `value`
        self._green = value
        
    @green.deleter
    def green(self):
        del self._green     
    
    @property
    def blue(self):
        """The blue channel.
        
        **Invariant**: value must be an int between 0 and 255, inclusive."""
        return self._blue
    
    @blue.setter
    def blue(self, value):
        assert (type(value) == int), "value %s is not an int" % `value`
        assert (value >= 0 and value <= 255), "value %s is outside of range [0,255]" % `value`
        self._blue = value
        
    @blue.deleter
    def blue(self):
        del self._blue     
 
    @property
    def alpha(self):
        """The alpha channel.
        
        Used for transparency effects (but not in this course).
        
        **Invariant**: value must be an int between 0 and 255, inclusive."""
        return self._alpha
        
    @alpha.setter
    def alpha(self, value):
        assert (type(value) == int), "value %s is not an int" % `value`
        assert (value >= 0 and value <= 255), "value %s is outside of range [0,255]" % `value`
        self._alpha = value
            
    @alpha.deleter
    def alpha(self):
        del self._alpha     

    # METHODS
    
    def __init__(self, r, g, b, a=255):
        """**Constructor**: creates a new RGB value (r,g,b,a).
        
            :param r: initial red value
            Precondition: int between 0 and 255, inclusive.
        
            :param g: initial green value
            Precondition: int between 0 and 255, inclusive.
        
            :param b: initial blue value
            Precondition: int between 0 and 255, inclusive.
        
            :param a: initial alpha value (default 255)
            Precondition: int between 0 and 255, inclusive.
        
        The alpha channel is 255 by default, unless otherwise specified."""        
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a
            
    def __eq__(self, otherColor):
        """Returns: True if self and otherColor are equivalent RGB colors. """
        return (type(otherColor) == RGB and self.red == otherColor.red and 
                self.green == otherColor.green and self.blue == otherColor.blue and
                self.alpha == otherColor.alpha)

    def __ne__(self, otherColor):
        """Returns: True if self and otherColor are not equivalent RGB colors. """
        return (type(otherColor) != RGB or self.red != otherColor.red or 
                self.green != otherColor.green or self.blue != otherColor.blue or
                self.alpha != otherColor.alpha)

    def __str__(self):
        """Returns: Readable string representation of this color. """
        return "("+str(self.red)+","+str(self.green)+","+str(self.blue)+","+str(self.alpha)+")"

    def __repr__(self):
        """Returns: Unambiguous String representation of this color. """
        return "(red="+str(self.red)+",green="+str(self.green)+",blue="+str(self.blue)+",alpha="+str(self.alpha)+")"

    def openGLColor(self):
        """**Returns**: 4 element list of the attributes in the range 0 to 1
        
        This is a conversion of this object into a format that can be used in
        openGL graphics"""
        return [self.red/255.0, self.green/255.0, self.blue/255.0, self.alpha/255.0]

# Color Constants

#: The color white in the default RGB space.
WHITE = RGB(255, 255, 255)

#: The color light gray in the default RGB space.
LIGHT_GRAY = RGB(192, 192, 192)

#: The color gray in the default RGB space.
GRAY = RGB(128, 128, 128)

#: The color dark gray in the default RGB space.
DARK_GRAY = RGB(64, 64, 64)

#: The color black in the default RGB space.
BLACK = RGB(0, 0, 0)

#: The color red, in the default RGB space.
RED = RGB(255, 0, 0)

#: The color pink in the default RGB space.
PINK = RGB(255, 175, 175)

#: The color orange in the default RGB space.
ORANGE = RGB(255, 200, 0)

#: The color yellow in the default RGB space.
YELLOW = RGB(255, 255, 0)

#: The color green in the default RGB space.
GREEN = RGB(0, 255, 0);

#: The color magenta in the default RGB space.
MAGENTA = RGB(255, 0, 255)

#: The color cyan in the default RGB space.
CYAN = RGB(0, 255, 255)

#: The color blue in the default RGB space.
BLUE = RGB(0, 0, 255)