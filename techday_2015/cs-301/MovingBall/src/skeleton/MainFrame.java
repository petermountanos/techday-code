package skeleton;
import stdlib.StdDraw;

/**
 * <i>MainFrame<i>. This simple main frame class is meant to teach object
 * oriented programming. It instantiates a custom ball class created by the
 * programmer, and animates that ball using loops. There are several constants
 * in this class which help facilitate programming in other classes.
 * 
 * @author  YOUR NAME HERE
 * @author  Peter Mountanos 
 * @author  Alyssa Kelly
 * @version 1.0
 * @since   January 6, 2014
 */
public class MainFrame {
	
	//-----------CONSTANTS-----------//
	/**
	 * Constant to represent the y position of the top wall of the frame
	 */
	public static final double TOP_WALL = 0.975;
	/**
	 * Constant to represent the y position of the bottom wall of the frame
	 */
	public static final double BOTTOM_WALL = 0.025;
	/**
	 * Constant to represent the x position of the left wall of the frame
	 */
	public static final double LEFT_WALL = 0.025;
	/**
	 * Constant to represent the x position of the right wall of the frame
	 */
	public static final double RIGHT_WALL = 0.975;
	
	/**
	 * Main method of the MainFrame class. This main method is called once the
	 * Java program is compiled and run. It contains a while loop, which allows 
	 * for the animation of the ball. It utilizes StdDraw methods to aid in the
	 * animation code. First, it instantiates a new Ball object, and within the
	 * loop, it checks the ball's boundaries and then moves the ball one step at
	 * a time.
	 */
	public static void main(String[] args) {
	
		// variables to help make a new ball
		double start_x = 0.5;
		double start_y = 0.5;
		double radius  = 0.05;
		
		// instantiate a new ball object
		Ball ballOne = new Ball(start_x, start_y, radius);
		
		// set the size of the drawing screen
		StdDraw.setCanvasSize(500,500);
		
		// animation code: turn off outside loop
		StdDraw.show();
		
		// infinite loop to move ball forever
		while (true) {
			// clear the screen and make the background gray
			StdDraw.clear(StdDraw.GRAY);
			
			// check the boundaries of the ball
			ballOne.checkBounds();
			
			// move the ball one step at a time
			ballOne.move();
			
			// animation code: pause for 10ms and start over
			StdDraw.show(10);
		}
	}
}
