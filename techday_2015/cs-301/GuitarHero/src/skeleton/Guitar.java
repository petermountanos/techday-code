package skeleton;
import stdlib.*;

/**
 * <i>Guitar<i>. The Guitar object emulates a guitar composed of multiple
 * GuitarString objects, where the frequencies of these strings is based on
 * the keyboard mapping given by the keyboard constant in this class.
 *  
 * An instance of this class is used for the GuitarHero app for CS.301 for 
 * Wantagh TechDay 2015.
 *
 * @author  YOUR NAME HERE
 * @author  Peter Mountanos 
 * @author  Alyssa Kelly
 * @version 1.0
 * @since   December 30, 2014
 */
public class Guitar {
	// CLASS CONSTANTS
	/**
	 * String constant storing the keys that corresponds to a certain note.
	 */
	public static final String keyboard = "q2we4r5ty7u8i9op-[=zxdcfvgbnjmk,.;/' ";
	/**
	 * Starting frequency for an A note.
	 */
	public static final int A440 = 440;

	// INSTANCE VARIABLES
	/**
	 * Array of GuitarStrings which simulates a guitar.
	 */
	private GuitarString[] strings;

	  /**
	   * Constructor which creates a Guitar object. A Guitar object is composed of 37 strings,
	   * which corresponds to how many keys on the keyboard will have a mapping. The constructor 
	   * needs to instantiate 37 GuitarString objects with the correct frequency, and store those
	   * in an array of strings.
	   */
	public Guitar() {

		//--------------------------------------//
		//------------YOUR CODE HERE------------//
		//--------------------------------------//
		
	}

	/**
	 * Method to simulate the playing of the guitar based on a note played.
	 * The note played is passed in as a parameter, when called from a Guitar
	 * instance object.
	 * 
	 * @param  key character represented key pressed, which represents a note
	 * @return a double representing the sample just played to be used for 
	 *		 visualization purposes in the GuitarHero class.
	 */
	public double play(char key) {

		//--------------------------------------//
		//------------YOUR CODE HERE------------//
		//--------------------------------------//

		return 'a';
	}
}
