package complete;
import stdlib.*;

/**
 * <i>Guitar<i>. The Guitar object emulates a guitar composed of multiple
 * GuitarString objects, where the frequencies of these strings is based on
 * the keyboard mapping given by the keyboard constant in this class.
 *  
 * An instance of this class is used for the GuitarHero app for CS.301 for 
 * Wantagh TechDay 2015.
 *
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
		// based on the keyboard string constant
		this.strings = new GuitarString[Guitar.keyboard.length()];

		// for each key, compute frequency
		for (int i = 0; i < this.strings.length; i++) {
			double frequency = Guitar.A440 * Math.pow(1.05956, (i - 24));
			this.strings[i] = new GuitarString(frequency);
		}
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

		// get key index from keyboard string
		int keyIndex = Guitar.keyboard.indexOf(key);

		// only pluck if the key hasn't been pressed
		if (keyIndex != -1) this.strings[keyIndex].pluck();

		// compute the combined sound of all notes
		double sample = 0;
		for (int i = 0; i < this.strings.length; i++) {
			sample += this.strings[i].sample();
		}

		// play the sample on standard audio
		StdAudio.play(sample);

		// advance the simulation of each harp string by one step   
		for (int i = 0; i < this.strings.length; i++) {
			this.strings[i].tic();
		}

		return sample;
	}

}
