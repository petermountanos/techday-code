package raffle;
import stdlib.*;

/**
 * <i>RouletteWheel<i>. This is a basic program that displays a roulette wheel GUI 
 * to simulate the drawing of a random winner from our feedback survey. The winner
 * will receive a prize. It parses a text file of names, one per line, that contain
 * all of the names who participated in the survey. It then stores these names in an
 * array and picks a random index of the array as a winner.
 * 
 * @author  Peter Mountanos 
 * @version 1.0
 * @since   January 10, 2015
 */
public class RouletteWheel {

	
	public static String src_file = "data/test.txt";
	public static double rotation = 5;
	public static double increment = 5;
	public static int counter = 700;
	
	/**
	 * Main method which is responsible for instantiating the GUI, playing
	 * the music, and calling a helper method to pick a random winner. The 
	 * roulette wheel image spins for as long as the sound effect is going,
	 * and then displays the winner's name at the bottom of the screen once
	 * the simulation is complete.
	 */
    public static void main(String[] args) {
    	// animation mode: turn off for now
    	StdDraw.show();
    	
    	// pick a random winner from text file
    	String winner = getRandomWinner();
    	
    	// start playing the music
    	StdAudio.play("data/roulette.wav");
    	
    	// loop until you've reached the end of the counter
    	while (counter > 0) {
    		// clear the screen
    		StdDraw.clear();

    		// header text
    		StdDraw.text(0.5, 0.95, "Wantagh TechDay Raffle");
    		
    		// draw the picture at a certain rotation % 360
    		StdDraw.picture(0.5, 0.5, "data/American_roulette-wheel.gif", rotation % 360);
    		
    		// footer text
    		StdDraw.text(0.5, 0.05, "Winner is: ");
    		
    		// increase rotation increment for "spinning" effect
    		rotation += increment;
    		
    		// animation mode: on, pause for 10 ms and loop
    		StdDraw.show(10);
    		
    		// deduct counter to reach end of loop
    		counter--;
    	}
    	
    	// turn off animation mode
    	StdDraw.show();
    	
    	// clear the screen and redraw everything, but with winner's name now
    	StdDraw.clear();
    	StdDraw.text(0.5, 0.95, "Wantagh TechDay Raffle");
    	StdDraw.picture(0.5, 0.5, "data/American_roulette-wheel.gif", rotation % 360);
    	StdDraw.text(0.5, 0.05, "Winner is: " + winner + "!!!");
    }
 
    /**
     * Helper method to parse the input file to pick a random winner from
     * the file. This method then returns the name of that random winner 
     * for the GUI to display at the appropriate time. 
     * 
     * @return string representing the name of the winner of the raffle.
     */
    public static String getRandomWinner() {
    	// instantiate a new In object to get input
    	In inStream = new In(src_file);
    	
    	// get number of contestants from first line of the file
    	int numContestants = inStream.readInt();
    	
    	// create array with size of number of contestants
    	String[] contestants = new String[numContestants];
    	
    	// add contestants to array (one per line)
    	for (int i = 0; i < numContestants; i++) {
    		contestants[i] = inStream.readLine();
    	}
    	
    	// pick a random index in the array
    	int randomIndex = StdRandom.uniform(numContestants);
    	
    	// return the name of the winner associated to random index
    	return contestants[randomIndex];
    }

   
}