package eqtn;
//VERSION 3

import java.util.*;

public class Const {
		
	public Const() {}
	
	public void add(ArrayList<Double> X, ArrayList<Double> Y) {
		pts = new double[2][X.size()];
		pts[0] = toDub(X);
		pts[1] = toDub(Y);
	}	
	
	public double[] solver(int n) {
		double[] eqtn = new double[n];
		int pow = n-1;
    
		for(int a=0; a <= pow; a++) {
			double sum = 0;
			for(int b=a; b>=1; b--)
				sum += eqtn[a-b]*mult(n-a, b, 0);
			eqtn[a] = lrgConst(n-a, pow-a) - sum;
		}
		return eqtn;
	}
	
	
	//START HELPER METHODS

	//calculates the constant of the largest x pow (eg d in dx^3+cx²+bx+a)
	public double lrgConst(int n, int pow) {
		if (n > 0)
		if (pow <= 0) {
			return pts[1][0];
		} else if (pow == 1) {
			return (pts[1][n-1] - pts[1][0])/(pts[0][n-1] - pts[0][0]);
		} else {
			return (lrgConst(n, pow-1)-lrgConst(n-1, pow-1))/(pts[0][n-1] - pts[0][n-pow]);
		}
		else
			return 0;
	}

	//calculates all possible ways of obtaining pow power with n number, a initiates as 0
	//eg 3, 1, 0 returns x1+x2+x3 -- 2, 3, 0 returns x1(x1(x1+x2)+x2(x2))+x2(x2(x2))
	public double mult(int n, int pow, int a) {
		double out = 0;
		
		if (pow < 1)
			out = 0;
		else if (pow == 1) { //sums x vals from a thru n-1 inclusively
			if (a<=n-1)
				for(int i=a; i<n; i++)
					out += pts[0][i];
		}
		else {
			for(int b=a; b<n; b++)
				out += pts[0][b]*mult(n, pow-1, b);
		}
		return out;
	}
	
	//convert from ArrayList Double to double[]
	public double[] toDub(ArrayList<Double> dub) {
		double[] out = new double[dub.size()];
		
		for (int i=0; i < dub.size(); i++)
			out[i] = dub.get(i).doubleValue();
		return out;
	}
		
	@Override
	public String toString() {
		String output = "y=";
		double[] out = solver(pts[0].length);
		
		for(int i=0; i<out.length;i++)
			if(out[i] != 0) {
				if((out[i] > 0) && (i > 0))
					output += "+";
				if(pts[0].length-i-1 > 1)
					output += out[i] + "x^" + (pts[0].length-i-1);
				else if(pts[0].length-i-1 > 0)
					output += out[i] + "x";
				else
					output += out[i];
			}
		return output;		
	}
	
	private double[][] pts;
}