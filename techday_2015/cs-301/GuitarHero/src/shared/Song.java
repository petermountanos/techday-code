package shared;
import stdlib.In;

/**
 * <i>Song<i>. This is a basic song class which reads in song files to
 * help visualize the notes on the GuitarHero App. The notes of the song
 * are stored in a 2d-array, where each sub-array represents a chord, which
 * could contain a max of five notes. There is also an internal iterator which
 * allows one to iterate through a song, which returns a note chord. This song
 * class is used for CS.301 for Wantagh TechDay 2015.
 *
 * @author  Peter Mountanos 
 * @author  Alyssa Kelly
 * @version 1.0
 * @since   December 30, 2014
 */
public class Song {
	// CLASS CONSTANTS
	/**
	 * 
	 */
	public static final int MAX_NOTES = 5;

	// INSTANCE VARIABLES
	/**
	 * 
	 */
	private In songFile;
	/**
	 * 
	 */
	public String[][] notes;
	/**
	 * 
	 */
	public double[] timing;
	/**
	 * 
	 */
	private int nextNote;

	/**
	 * 
	 * @param src
	 */
	public Song(String src) {
		this.songFile = new In(src);
		this.parseFile();
		this.nextNote = 0;
	}

	/**
	 * 
	 */
	private void parseFile() {
		int numNotes = songFile.readInt();

		this.notes  = new String[numNotes][MAX_NOTES];
		this.timing = new double[numNotes];

		for (int i = 0; i < numNotes; i++) {
			for (int j = 0; j < MAX_NOTES; j++) {
				this.notes[i][j]  = songFile.readString();
			}
			this.timing[i] = songFile.readDouble();
		}
	}

	/**
	 * 
	 * @return
	 */
	public boolean hasNext() {
		return this.nextNote < this.notes.length;
	}

	/**
	 * 
	 * @return
	 */
	public String nextNote() {
		String returnNote = "FINISHED";

		if (this.hasNext()) {
			String[] notes = this.notes[this.nextNote];
			returnNote = "";
			int i = 0;
			while (i < MAX_NOTES && !notes[i].equals("-")) {
				returnNote += notes[i] + " ";
				i++;
			}
		}
		this.nextNote++;
		return returnNote;
	}
}
