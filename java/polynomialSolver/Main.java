//Steven Williams - Major code completed 4/30/2015

import java.util.*;

//VERSION 2 USES Solve(), VERSION 3 USES Const()

public class Main {	
	public static void main(String[] args) {
		ArrayList<Double> X = new ArrayList<Double>();
		ArrayList<Double> Y = new ArrayList<Double>();
		in = new Scanner(System.in);
		int count = 0;
		//Solve eqtn = new Solve();
		Const eqtn = new Const();
	
		System.out.println("Enter a point twice to exit input loop");
		while (X.size() >= 0) {		//loops forever
			System.out.print("X"+(count+1)+":");
			double xIn = in.nextDouble();
			if (!X.contains(xIn)) {			//if x-list doesn't contain input, continue, else break
				X.add(xIn);
				System.out.print("Y"+(count+1)+":");
				double yIn = in.nextDouble();
				Y.add(yIn);
				count++;
				eqtn.add(X, Y);
				System.out.println(eqtn);			//displays eqtn nums after every pt added
			} else {
				break;
			}
		}	
	}
	private static Scanner in;
}




/*  //VERSION 1
import java.util.Scanner;

public class Main {
 
 public static void main(String[] args) {
  //pts x  1  2  3
  //    y  1  4  9
  
  double[][] pts = new double[2][5];
  int pow = pts[0].length-1;
  Scanner in = new Scanner(System.in);
  
  for (int count = 0; count < pts[0].length; count++) {
   System.out.print("X"+(count+1)+":");
   pts[0][count] = in.nextDouble();
   
   System.out.print("Y"+(count+1)+":");
   pts[1][count] = in.nextDouble();
  }
  
  double out = recur(pts, pts[0].length-1, pow);
  
  System.out.print(out);
 }
 
 
 public static double recur(double[][] pts, int n, int pow) {
  
  if (pow == 1) {
   return (pts[1][n] - pts[1][0])/(pts[0][n] - pts[0][0]);
  } else {
   return (recur(pts, n, pow-1)-recur(pts, n-1, pow-1))/(pts[0][n] - pts[0][n-pow+1]);
  }
 }
 
}
*/