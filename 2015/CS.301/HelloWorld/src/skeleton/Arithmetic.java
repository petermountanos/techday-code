package skeleton;

/**
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
public class Arithmetic {
	public static void main(String[] args) { 
		
		//-------INTEGERS-------//
		int a = 4;
		int b = 6;
	
		System.out.println(a + b);
		System.out.println(b - a);
		System.out.println(a * b);
		System.out.println(b / a);
		System.out.println(b % a);
		
		//-------DOUBLES-------//
		double c = 10.2;
		double d = 2.00;
		
		System.out.println(c + d);
		System.out.println(c - d);
		System.out.println(c * d);
		System.out.println(c / d);
		
		//------BOOLEANS------//
		boolean e = true;
		boolean f = true;
		boolean g = false;
		boolean h = false;
		
		System.out.println(e && f);
		System.out.println(f && h);
		System.out.println(e || g);
		System.out.println(g || h);
		System.out.println(!g);
		System.out.println(!e);
		
		//-------STRINGS------//
		String i = "Intro to ";
		String j = "Java";
		
		System.out.println(i + j);
	}
}
