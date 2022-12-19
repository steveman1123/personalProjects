package eqtn;
//VERSION 2: WILL ONLY CALCULATE FIRST 3 COEFFICIENTS

import java.util.*;

public class Solve {
	
	public Solve() {}
	
	public void add(ArrayList<Double> X, ArrayList<Double> Y) {
		pts = new double[2][X.size()];
		pts[0] = toDub(X);
		pts[1] = toDub(Y);
	}
	
	//n=current subscript number (eg x1 vs x2), pow=current power (eg x^1 vs x^2)
	
	//solve for largest constant (eg c in cx²+bx+a or d in dx^3+cx²+bx+a)
	public double A(int n, int pow) {
		if (pow == 0) {
			return pts[1][0];
		} else if (pow == 1) {
			return (pts[1][n] - pts[1][0])/(pts[0][n] - pts[0][0]);
		} else {
			return (A(n, pow-1)-A(n-1, pow-1))/(pts[0][n] - pts[0][n-pow+1]);
		}
	}
	
	//solve for next largest (eg b in cx²+bx+a or c in dx^3+cx²+bx+a)
	public double B(int n, int pow) {
		double sum = 0;
		sum = sumX(0,pts[0].length-2);
		return A(n-1, pow-1)-A(n, pow)*sum;
	}
	
	//solve for 3rd num (eg a in cx²+bx+a or b in dx^3+cx²+bx+a)
	public double C(int n, int pow) {
		double a = A(n, pow);
		double b = B(n, pow);
		double out = 0;
		for(int i = 0; i < pts[0].length-2; i++)
			out += pts[0][i]*sumX(i, pts[0].length-3);
		out = A(n-2, pow-2) - (a*out+b*sumX(0, pts[0].length-3));
		return out;
	}

	//convert from ArrayList Double to double[]
	public double[] toDub(ArrayList<Double> dub) {
		double[] out = new double[dub.size()];
		for (int i=0; i < dub.size(); i++)
			out[i] = dub.get(i).doubleValue();
		return out;
	}
	
	//sum section of array btw s (start) & e (end)
	public double sumX(int s, int e) {
		int sum = 0;
		for(int i = s; i <= e; i++)
			sum += pts[0][i];
		return sum;
	}
	
	
	//format to String
	@Override
	public String toString() {
		String out = "";
		//adds a number after every added pt
		if (pts[0].length > 0)	out += A(pts[0].length-1, pts[0].length-1) + "    ";
		if (pts[0].length > 1)	out += B(pts[0].length-1, pts[0].length-1) + "    ";
		if (pts[0].length > 2)	out += C(pts[0].length-1, pts[0].length-1) + "    ";
		
		return out;
	}
	
	double[][] pts;
}
