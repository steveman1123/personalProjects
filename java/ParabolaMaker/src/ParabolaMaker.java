//import java.util.Arrays;
import java.util.Scanner;


public class ParabolaMaker {

	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		
		
		System.out.print("How many points do you know? (1-4) ");
		int num = in.nextInt();
		if (num > 4 || num < 1) { 
			System.out.println("Out of Range.");
			System.exit(1);
		}
		
		double[][] numList = new double[2][num];
		
		for (int count = 0; count<num; count++) {
			System.out.print("X"+(count+1)+":");
			numList[0][count] = in.nextDouble();
			
			System.out.print("Y"+(count+1)+":");
			numList[1][count] = in.nextDouble();
		}
		
		
		
		Equation one = new Equation(numList[0], numList[1]);
		
		System.out.println(one.Solve());
		
		
		in.close();
	}
}
