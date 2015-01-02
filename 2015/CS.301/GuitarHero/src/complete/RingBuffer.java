package complete;

/**
 * <i>Ring Buffer<i>. The ring buffer is implemented using a circular queue,
 * which is a FIFO (first in, last out) data structure. This class provides a
 * basic buffer capabilities to efficiently store streaming data in memory. 
 * 
 * The buffer will be used to store note frequencies for the GuitarHero app
 * for CS.301 for Wantagh TechDay 2015.
 *
 * @author  Peter Mountanos 
 * @author  Alyssa Kelly
 * @version 1.0
 * @since   December 30, 2014
 */

public class RingBuffer {
	/**
	 * Array storing the items in the ring buffer.
	 */
    private double[] rb;
    /**
     * Integer storing the current index for the next spot to dequeue or peek.
     */
    private int first;
    /**
     * Integer storing the current index for the next spot to enqueue.
     */
    private int last;
    /**
     * Integer storing the number of items in the buffer.
     */
    private int size;

    /**
     * Constructor which instantiates an empty RingBuffer object,
     * with a given max capacity based on parameter input.
     * 
     * @param capacity integer determining the max capacity of the buffer.
     */
    public RingBuffer(int capacity) {
        // instantiate array of size capacity
        this.rb    = new double[capacity];
        this.first = 0;
        this.last  = 0;
        this.size  = 0;
    }

    /**
     * Method which returns the number of items currently being stored in the
     * RingBuffer object.
     * 
     * @return an integer representing the current number of items stored in 
     *         the buffer.
     */
    public int size() {
        return this.size;
    }

    /**
     * Method which determines if the RingBuffer object is empty, and returns
     * a truth value based on the current status.
     *  
     * @return true if the buffer object is empty, else false.
     */
    public boolean isEmpty() {
        return this.size == 0;
    }

    /**
     * Method which determines if the RingBuffer object is full, and returns
     * a truth value based on the current status.
     * 
     * @return true if the buffer object if full, else false.
     */
    public boolean isFull() {
        return this.size == this.rb.length;
    }
    
    /**
     * Method which returns the capacity of the current RingBuffer Object.
     * 
     * @return integer representing the capacity of the buffer.
     */
    public int getCapacity() {
    	return this.size;
    }
    /**
     * Method to add an item to the end of the buffer object. If one tries
     * to add an item to a full ring buffer object, a runtime exception is 
     * thrown.
     * 
     * @param item note to be be added to the end of the buffer.
     * @throws RuntimeException if the ring buffer object is full when called.
     */
    public void enqueue(double item) {
    	// if the buffer is at capacity, throw error
        if (isFull()) {
            throw new RuntimeException("Ring buffer overflow");
        }
        
        // enqueue and increment index counter
        this.rb[this.last] = item;
        this.last++;
        
        // cyclical wrap-around implementation
        if (this.last == this.rb.length) this.last = 0;
        
        this.size++;
    }

    /**
     * Method to remove the first item from the buffer object. This
     * method returns the first item from the buffer object, and then
     * deletes it. If the buffer is empty, it throws a runtime error.
     * 
     * @throws RuntimeException if the ring buffer object is empty when called.
     * @return the first item from the buffer object, to be remove.
     */
    public double dequeue() {
    	// if the buffer is empty, throw a runtime error
        if (isEmpty()) {
            throw new RuntimeException("Ring buffer underflow");
        }
        
        // store front of queue in temp variable and then "delete"
        double temp = this.rb[this.first];
        this.first++; 
        
        // cyclical wrap-around implementation
        if (this.first == this.rb.length) this.first = 0;
        this.size--;
        
        return temp;
    }

    /**
     * Method to return, but not delete, the item at the front of 
     * the buffer. If the buffer is empty, it throws a runtime 
     * exception.
     * 
     * @throws RuntimeException if the ring buffer object is empty when called.
     * @return
     */
    public double peek() {
        // if the buffer is empty, throw exception
    	if (isEmpty()) {
            throw new RuntimeException("Ring buffer underflow");
        }
        
        return this.rb[this.first];
    }

    /*
     * (non-Javadoc)
     * @see java.lang.Object#toString()
     */
    public String toString() {
    	// instantiate a new string buffer to store string
    	StringBuffer sb = new StringBuffer("Ring Buffer: [");
    	
    	// return a [] to represent empty buffer
    	if (this.size == 0) return sb.append("], Size: 0").toString();
    	
    	// iterate through buffer and append items onto string buffer
    	int current = this.first;
    	for (int i = 0; i < this.size; i++) {
    		sb.append(rb[current] + ", ");
    		current++;
    		
    		// account for cyclical wrap-around
    		if (current == this.rb.length) current = 0;
     	}
    	
    	// replace the last comma and space with a closing bracket and return 
    	sb.delete(sb.length()-2, sb.length());
    	sb.append("]");
    	
    	return sb.toString();
    }
    
    /**
     * Main method to run a few tests to make sure the ring buffer class 
     * is configured properly.
     * 
     * @param args array of string arguments passed in as cmd-line input.
     */
    public static void main(String[] args) {
    	
    	// verify there's only one command line parameter
    	if (args.length != 1) {
    		System.err.println("Usage: java bufferSize");
    		System.exit(1);
    	}
    	
    	// instantiate new buffer of the size of the input and 
    	// enqueue numbers 1 - N
        int N = Integer.parseInt(args[0]);
        RingBuffer buffer = new RingBuffer(N);
        for (int i = 1; i <= N; i++) {
            buffer.enqueue(i);
        }
        
        // dequeue and then re-enqueue it
        double t = buffer.dequeue();
        buffer.enqueue(t);
        
        // test cyclical wrap around capabilities
        System.out.println("Size after wrap-around is " + buffer.size());

        // until buffer size is two, dequeue two numbers and enqueue their sum 
        while (buffer.size() >= 2) {
            double x = buffer.dequeue();
            double y = buffer.dequeue();
            buffer.enqueue(x + y);
        }

        // print out the next item of the queue to be dequeued
        System.out.println(buffer.peek());
        
    }
}
