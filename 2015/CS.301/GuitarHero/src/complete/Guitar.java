package complete;

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

	// CLASS VARIABLES
	/**
	 * Array of GuitarStrings which simulates a guitar.
	 */
	public static GuitarString[] strings;

	/**
	 * Main Method to initialize the virtual guitar and detect keyboard input
	 * so a user can play the guitar.
	 * 
	 * @param args array of cmd-line arguments, not expecting anything.
	 */
	public static void main(String[] args) {

		// print out notes to give user something to play
		System.out.println("Stairway to Heaven Intro:");
		System.out.println("                                              w q q");
		System.out.println("        8       u       7       y             o p p");
		System.out.println("i p z v b z p b n z p n d [ i d z p i p z p i u i i");

		// create 37 harp strings represented by keyboard
		initializeKeyBoard();

		// listen for keyboard input and play notes
		while (true) {
			// if key was pressed get it and play the corresponding note
			if (StdDraw.hasNextKeyTyped()) {
				char key = StdDraw.nextKeyTyped();

				// find index of which key was pressed
				int keyIndex = keyboard.indexOf(key);
				// only pluck if the key hasn't been pressed
				if (keyIndex != -1) strings[keyIndex].pluck();
			}

			// compute the combined sound of all notes
			double sample = 0;
			for (int i = 0; i < strings.length; i++) {
				sample += strings[i].sample();
			}

			// play the sample on standard audio
			StdAudio.play(sample);

			// advance the simulation of each harp string by one step   
			for (int i = 0; i < strings.length; i++) {
				strings[i].tic();
			}
		}
	}

	/**
	 * Helper method to initialize an array of strings which corresponding
	 * to a set of keys on the user's keyboard.
	 */
	public static void initializeKeyBoard() {
		// based on the keyboard string constant
		strings = new GuitarString[keyboard.length()];

		// for each key, compute frequency
		for (int i = 0; i < strings.length; i++) {
			double frequency = A440 * Math.pow(1.05956, (i - 24));
			strings[i] = new GuitarString(frequency);
		}
	}
}
