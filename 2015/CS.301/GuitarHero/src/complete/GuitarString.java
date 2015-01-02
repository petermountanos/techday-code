package complete;

/**
 * <i>Guitar String<i>. The guitar string object emulates a vibrating guitar
 * string based on a certain frequency. A collection of guitar strings
 * allows one to simulate a full guitar with varying frequencies. The string
 * uses a default sampling rate of 44,100.
 *  
 * A collection of these string objects will be used for the GuitarHero app
 * for CS.301 for Wantagh TechDay 2015.
 *
 * @author  Peter Mountanos 
 * @author  Alyssa Kelly
 * @version 1.0
 * @since   December 30, 2014
 */

public class GuitarString {

	// CLASS CONSTANTS 
	/**
	 * Sampling rate is the number of samples of audio carried per second.
	 */
    public static final int SAMPLING_RATE   = 44100;  
    /**
     * Constant used to model the slight dissipation of energy as the wave 
     * makes a  round-trip through the string
     */
    public static final double ENERGY_DECAY = 0.994;
    
    // INSTANCE VARIABLES
    /**
     * RingBuffer to model the medium in which the energy travels back and forth.
     */
    private RingBuffer buffer;
    
    /**
     * Integer storing the number of times the tics method has been called. 
     */
    private int numTics;
    
    
    /**
     * Constructor which instantiates a GuitarString object of the given
     * frequency based on the parameter value passed in. 
     * 
     * @param frequency double representing the frequency of the guitar
     * 		  string to be created.
     */
    public GuitarString(double frequency) {
        // calculate desired capacity of the buffer based on frequency
        int N = (int) Math.ceil(GuitarString.SAMPLING_RATE / frequency);
        
        // initialize harp string at rest by enqueueing N 0's
        this.buffer = new RingBuffer(N);
        for (int i = 0; i < N; i++) {
            this.buffer.enqueue(0.0);
        }
        
        // set number of tics to be zero
        this.numTics  = 0;
    }

    /**
     * Constructor which instantiates a GuitarString object with its size
     * and initial values given by an array passed in as input.
     * 
     * @param init array of doubles containing the initial values of the buffer
     */
    public GuitarString(double[] init) {
        // create RingBuffer of size of init array
        this.buffer = new RingBuffer(init.length);
        
        // initialize the contents of the buffer to be the values
        // of the init array
        for (int i = 0; i < init.length; i++) {
            this.buffer.enqueue(init[i]);
        }
        
        // set number of tics to be zero
        this.numTics = 0;
    }

    /**
     * Method to simulate the plucking of a guitar string by replacing the
     * buffer with white noise. White noise is just replacing the each of the
     * N displacements to a real random number between -1/2 and +1/2.
     */
    public void pluck() {
    	
    	// for each N displacement point in the buffer
        for (int i = 0; i < buffer.getCapacity(); i++) { 
        	
            // white noise is random values in range (-0.5, 0.5)
            double whiteNoise = Math.random() - 0.5;
            
            // first remove current "first" value
            this.buffer.dequeue();
            
            // then add the random whiteNoise value to end of buffer
            this.buffer.enqueue(whiteNoise);
        }
    }

    /**
     * Simulate the plucking of the guitar string via the Karplus-Strong 
     * algorithm implementation. 
     */
    public void tic() {
        // remove and get value of first sample
        double sampleOne = this.buffer.dequeue();
        
        // get value of new first sample
        double sampleTwo = this.buffer.peek();
        
        // get average of two first samples, scaled by energy decay factor
        double update = 0.5 * (sampleOne + sampleTwo) * GuitarString.ENERGY_DECAY;
        
        // add calculated sample to end of the buffer
        this.buffer.enqueue(update);
        
        // increment number of times tics() has been called for this harp string
        this.numTics++;
    }

    /**
     * Method to return the current sample, which is the value of the
     * item at the front of the ring buffer.
     * 
     * @return the value of the item at the front of the buffer instance variable
     */
    public double sample() {
        return this.buffer.peek();
    }

    // return number of times tic was called
    public int time() {
    	 return this.numTics;
    }
    
    public RingBuffer getBuffer() {
    	return this.buffer;
    }

    /**
     * Main method to run a few tests to make sure the ring buffer class 
     * is configured properly.
     * 
     * @param args array of string arguments passed in as cmd-line input.
     */
    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        double[] samples = { .2, .4, .5, .3, -.2, .4, .3, .0, -.1, -.3 };  
        GuitarString testString = new GuitarString(samples);
        for (int i = 0; i < N; i++) {
            int t = testString.time();
            double sample = testString.sample();
            System.out.printf("%6d %8.4f\n", t, sample);
            testString.tic();
        }
    }

}