import java.util.Arrays;
public class Equation {


	public Equation(double[] xIn,  double[] yIn) {
		x = xIn;
		y = yIn;
	}
	
	
	public String Solve() {
		
		eqtn = new double[x.length];
		//y = a
		if (x.length == 1) {
			type = "y = a";
			eqtn[0] = y[0];
		}
		
		//y = bx + a
		if (x.length == 2) {
			type = "y = bx + a";
			eqtn[0] = (y[1]-y[0])/(x[1]-x[0]);
			eqtn[1] = y[0]-eqtn[0] * x[0];			
		}
		
		//y = cx^2 + bx + a
		if (x.length == 3) {
			type = "y = cx^2 + bx + a";
			eqtn[0] = ((y[2]-y[0])/(x[2]-x[0])-(y[1]-y[0])/(x[1]-x[0]))/(x[2]-x[1]);
			eqtn[1] = (y[1]-y[0])/(x[1]-x[0]) - eqtn[0]*(x[0]+x[1]);
			eqtn[2] = y[0] - x[0]*(eqtn[0]*x[0]+eqtn[1]);
		}

		//y = dx^3 + cx^2 + bx + a
		if (x.length == 4) {
			type = "y = dx^3 + cx^2 + bx + a";
			eqtn[0] = (((y[3]-y[0])/(x[3]-x[0])-(y[2]-y[0])/(x[2]-x[0]))/(x[3]-x[2])-((y[2]-y[0])/(x[2]-x[0])-(y[1]-y[0])/(x[1]-x[0]))/(x[2]-x[1]))/(x[3]-x[1]);
			eqtn[1] = ((y[2]-y[0])/(x[2]-x[0])-(y[1]-y[0])/(x[1]-x[0]))/(x[2]-x[1]) - eqtn[0]*(x[0]+x[1]+x[2]);
			eqtn[2] = (y[1]-y[0])/(x[1]-x[0]) - (eqtn[0]*(x[0]*x[0] + x[0]*x[1] + x[1]*x[1]) + eqtn[1]*(x[0] + x[1]));
			eqtn[3] = y[0] - x[0]*(x[0]*(eqtn[0]*x[0]+eqtn[1])+eqtn[2]);
		}		
		return type + "\n" + Arrays.toString(eqtn);
	}
	
	
	private double[] x;
	private double[] y;
	private double[] eqtn;
	private String type;
	
	
	
}
