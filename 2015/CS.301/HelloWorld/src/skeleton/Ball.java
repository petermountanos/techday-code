package skeleton;
import stdlib.*;

public class Ball {
	
	public static final double SPEED_X = 0.015;
	public static final double SPEED_Y = 0.023;
	private double x;
	private double y;
	private double vx;
	private double vy;
	private double radius;
	
	public Ball(double x, double y, double r) {
		this.x      = x;
		this.y      = y;
		this.radius = r;
		this.vx     = Ball.SPEED_X; 
		this.vy     = Ball.SPEED_Y;
	}
	
	public void move() {
		this.x += this.vx;
		this.y += this.vy;
	
		StdDraw.filledCircle(this.x, this.y, this.radius);	}
	
	public void checkBounds() {
		double left   = this.x - this.radius / 2.0;
		double right  = this.x + this.radius / 2.0;
		double top    = this.y + this.radius / 2.0;
		double bottom = this.y - this.radius / 2.0;
		
		if (top > MainFrame.TOP_WALL || bottom < MainFrame.BOTTOM_WALL) this.vy *= -1.0;
		
		if (left < MainFrame.LEFT_WALL || right > MainFrame.RIGHT_WALL) this.vx *= -1.0;
	}
}