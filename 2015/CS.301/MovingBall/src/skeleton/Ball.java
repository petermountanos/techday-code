package skeleton;
import stdlib.StdDraw;

/**
 * <i>Ball<i>. This simple ball class is meant to teach object oriented
 * programming. The ball has a position, velocity and radius properties.
 * It also has methods to check the boundaries of the ball, which allows
 * it to "bounce" off of the walls. It also has a method to move the ball
 * according to its velocity components. The constructor (method which
 * instantiates a new Ball object) sets these properties to their initial
 * values.
 *
 * @author  YOUR NAME HERE
 * @author  Peter Mountanos 
 * @author  Alyssa Kelly
 * @version 1.0
 * @since   January 6, 2014
 */
public class Ball {
	
	//-----------CONSTANTS-----------//
	/**
	 * Constant to represent the x-component of any ball's speed
	 */
	public static final double SPEED_X = 0.015;
	/**
	 * Constant to represent the y-component of any ball's speed
	 */
	public static final double SPEED_Y = 0.023;
	
	//----------PROPERTIES----------//
	/**
	 * X position component of the ball.
	 */
	private double x;
	/**
	 * Y position component of the ball.
	 */
	private double y;
	/**
	 * X velocity component of the ball.
	 */
	private double vx;
	/**
	 * Y velocity component of the ball.
	 */
	private double vy;
	/**
	 * Radius of the circular ball.
	 */
	private double radius;

	/**
	 * Constructor which instantiates a new Ball object, based
	 * on the position components and radius given. The velocity
	 * components of any ball objects are constant.
	 * 
	 * @param x double representing starting x position of new ball 
	 * @param y double representing starting y position of new ball
	 * @param r double representing the radius of the new ball
	 */
	public Ball(double x, double y, double r) {
		this.x      = x;
		this.y      = y;
		this.radius = r;
		this.vx     = Ball.SPEED_X; 
		this.vy     = Ball.SPEED_Y;
	}
	
	/**
	 * Helper method to move the ball one step based on its x and y
	 * velocity components. It then redraws the ball in its new position.
	 */
	public void move() {
		
		//--------------------------------------//
		//------------YOUR CODE HERE------------//
		//--------------------------------------//
		
	}
	
	/**
	 * Helper method to check the boundaries of the ball. If the ball collides
	 * with any of the walls, the appropriate component of the velocity must
	 * be negated (to "bounce" the ball off of that wall).
	 */
	public void checkBounds() {

		//--------------------------------------//
		//------------YOUR CODE HERE------------//
		//--------------------------------------//
		
	}
}
