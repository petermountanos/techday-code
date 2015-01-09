//-------------------------------------------------------//
//-------------------------------------------------------//
//-------------DO NOT EDIT CODE IN THIS FILE-------------//
//-------------------------------------------------------//
//-------------------------------------------------------//
package skeleton;
import stdlib.*;
import shared.Song;
import java.util.*;

/**
 * 
 * <i>GuitarHero<i>. This GuitarHero class is the main class for the GuitarHero
 * app for CS.301 for Wantagh TechDay 2015. It is responsible for instantiating 
 * a guitar object, and listening for keyboard input to play the correct frequencies
 * corresponding to the keyboard mapping. It is also responsible for the visualization
 * of the sound waves to add a nice effect.
 * 
 * @author  Peter Mountanos 
 * @author  Alyssa Kelly
 * @version 1.0
 * @since   December 30, 2014
 */
public class GuitarHero {

	public static Guitar myGuitar;
	public static Song   mySong;
	public static LinkedList<Double> wave;
	public static double sample;

	/**
	 * Main method which is called on the start up of the GuitarHero app program.
	 * This method instantiates all of the necessary objects to play the guitar and
	 * visualize its sound waves. It has a keyboard listener to detect keystrokes 
	 * which correspond to specific frequencies on the guitar.
	 */
	public static void main(String[] args) {

		// set canvas scale
		StdDraw.setXscale(0, 500);
		StdDraw.setYscale(-250, 250);

		// instantiate new Guitar and Song objects
		myGuitar = new Guitar();
		mySong   = new Song("data/stairway.txt");

		// print out notes to give user something to play
		System.out.println("Stairway to Heaven Intro:");
		System.out.println("                                              w q q");
		System.out.println("        8       u       7       y             o p p");
		System.out.println("i p z v b z p b n z p n d [ i d z p i p z p i u i i");

		// store sample waves in a LinkedList for visualization effects
		wave = new LinkedList<Double>();
		
		for (int i = 0; i < 500; i++) {
			wave.push((double)0);
		}

		// variables for visualization
		int counter = 0;

		// continuously loop playing noise
		while (true) {

			// set key pressed to default null character
			char key = '\u0000';

			// keep track of counter variable for visualization
			if (counter > 10000000) {
				counter = 0;
			}
			else { 
				counter++;
			}

			// if actual key was pressed get it
			if (StdDraw.hasNextKeyTyped()) {
				key = StdDraw.nextKeyTyped();
			}

			// play the correct note
			sample = myGuitar.play(key);

			// draw visualization
			wave.push(sample);
			wave.remove(wave.size()-1);
			if (counter % 1000 == 0) drawVisualization();
		}
	} 

	/**
	 * Helper method to draw the sound wave visualization onto the screen. When
	 * the counter meets a certain condition, this method is called. It first 
	 * clears the screen and draws a line connecting each point in the wave to 
	 * display it onto the screen.
	 */
	private static void drawVisualization() {
		// set animation mode to zero pause
		StdDraw.show(0);

		// clear the screen to remove old waves
		StdDraw.clear();

		// for each point in the wave draw a line to make a full wave
		for (int i = 0; i < wave.size() - 1; i++) {
			StdDraw.line(i, wave.get(i) * 150, i + 1, wave.get(i + 1) * 150);
		}

		// set animation mode to zero pause
		StdDraw.show(0);
	}
}
