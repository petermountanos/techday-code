package hw02;


public class NBody {

	public static void main(String[] args){
		/*VALIDATE COMMAND-LINE ARGUMENTS*/
		if (args.length != 3){
            System.err.println("Usage:  java NBody <filename>");
            System.exit(1);
		}
		
		/*CONSTANTS*/
		String PATH = "nbody_data/";
		double G = 6.67e-11;
		
		/*PARSE INPUT FOR DATA*/
		String filename = args[2]; // filename is the the name of your file
		In inStream = new In(filename); // creates a variable inStream that we can use to read from the file

		int N = inStream.readInt();
		double R = inStream.readDouble();		
		double[] m = new double[N];
		double[] px = new double[N];
		double[] py = new double[N];
		double[] vx = new double[N];
		double[] vy = new double[N];

		String[] image = new String[N];

		for (int i = 0; i < N; i++){
			m[i] = inStream.readDouble();
			px[i] = inStream.readDouble();
			py[i] = inStream.readDouble();
			vx[i] = inStream.readDouble();
			vy[i] = inStream.readDouble();
			image[i] = inStream.readString();
		}
		
		/*SET UP SCALE*/
		StdDraw.setXscale(-R,R);
		StdDraw.setYscale(-R,R);
		
		/*MOVE PLANETS*/
		double T  = Double.parseDouble(args[0]);
		double dt = Double.parseDouble(args[1]);
		double timeElapsed = 0;
		
		while (timeElapsed < T){
			StdDraw.picture(0, 0, PATH+"starfield.jpg");
			
			for (int i = 0; i < N; i++){
				double Fx = 0;
				double Fy = 0;
				for (int other = 0; other < N; other++){
					if (i != other){
						double deltaX = (double) px[other] - px[i];
						double deltaY = py[other] - py[i];
						double d = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
						double F = (G * m[i] * m[other]) / (d * d);
						Fx += F * (deltaX / d);
						Fy += F * (deltaY / d);
					}
				}
				double ax = Fx / m[i];
				double ay = Fy / m[i];
				vx[i] += ax * dt;
				vy[i] += ay * dt;
			}
			
			for (int j = 0; j < N; j++){
				px[j] += vx[j] * dt;
				py[j] += vy[j] * dt;
				StdDraw.picture(px[j], py[j], PATH+image[j]);
			}
			StdDraw.show(20); // animation speed
			timeElapsed += dt;
		}
		System.out.printf("%d\n", N);
		System.out.printf("%.2e\n", R);
		for (int i = 0; i < N; i++) {
		    System.out.printf("%12.5e %12.5e %12.5e %12.5e %12.5e %12s\n",
		                   m[i], px[i], py[i], vx[i], vy[i], image[i]);
		}
	}
}
