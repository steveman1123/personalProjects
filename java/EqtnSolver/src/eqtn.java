import java.util.ArrayList;

public class eqtn{
	
	public eqtn(ArrayList<Double> X, ArrayList<Double> Y) {
		pts = new double[2][X.size()];
		pts[0] = toDub(X);
		pts[1] = toDub(Y);	
	}
	

	
	
	
	
	
	public double summer(int start, int end, int pow) {
		double sum = 0;
		if (!((end < start) || (start <= 0) || (end >= pts.length))) {
			
		}
		
		return sum;
	}	
	
	//convert from ArrayList Double to double[]
	public double[] toDub(ArrayList<Double> dub) {
		double[] out = new double[dub.size()];
		for (int i=0; i < dub.size(); i++)
			out[i] = dub.get(i).doubleValue();
		return out;
	}	

	private double[][] pts; //row 0 = X's, row 1 = Y's
}
