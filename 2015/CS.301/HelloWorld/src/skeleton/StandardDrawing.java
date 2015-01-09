package skeleton;
import stdlib.StdDraw;

/**
 * <i>StandardDrawing<i>. This class shows off some basic shapes and 
 * usage for the standard draw library. 
 * 
 * @author  Peter Mountanos 
 * @author  Alyssa Kelly
 * @version 1.0
 * @since   December 30, 2014
 */
public class StandardDrawing {

	// main method which runs on start of program
	public static void main(String[] args) {
		double rectangleX = 0.25;
		double rectangleY = 0.75;
		double halfWidth  = 0.25;
		double halfHeight = 0.25;
		double circleX    = 0.75;
		double circleY    = 0.25;
		double radius     = 0.25;
		
		StdDraw.setCanvasSize(500, 500);
		StdDraw.setPenColor(StdDraw.PINK);
		StdDraw.filledRectangle(rectangleX, rectangleY, halfWidth, halfHeight);
		StdDraw.setPenColor(StdDraw.YELLOW);
		StdDraw.filledCircle(circleX, circleY, radius);
	}
}
