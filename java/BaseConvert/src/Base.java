//import java.math.BigInteger;

public class Base {

	public Base (String baseIn, String baseOut, String numIn) {
	    	    
	    bIn = Integer.parseInt(baseIn);
	    bOut = Integer.parseInt(baseOut);
	    num = numIn;
		
	    char chr = '0';
	    int chrVal = 0;
     
	     if (bIn < 2 || bOut < 2 || bIn > 62 || bOut > 62){
	     	System.out.println("Wrong!!");
	     	System.exit(1);
	     } else {
	     		    
	 	    //convert from string to long, baseIn to base 10
	 	    for (int l = num.length()-1; l >= 0; l--) {
	 	      chr = num.charAt(num.length() - (l + 1));
	 	      chrVal = chr;   
	 	      //acsii vals to b10 nums, 0-9=0-9, A-Z=10-35, a-z=36-61
	 	      if (chrVal > 47 && chrVal < 58) { chrVal -= 48; }
	 	      else 
	 	      if (chrVal > 64 && chrVal < 91) { chrVal -= 55; }
	 	      else
	 	      if (chrVal > 96 && chrVal < 123) { chrVal -= 61; }
	 	      else { //makes sure that the input is valid, eg no symbols
	 	    	 System.out.println("Wrong!!");
	 	    	 System.exit(1);
	 	      }
	 	    	  
	 	      //indicates that the input number doesn't go beyond the input base
	 	      if (chrVal < bIn && chrVal > -1) {
	 	    	  totalVal += chrVal * Math.pow(bIn, l);
	 	      } else {
	 	    	  System.out.println("Wrong!!");
	 	    	  System.exit(1);
	 	      }
	 	    }
	 	    
	 	    //get length of new output number
	 	    double xCount = 0;
	 	    while ((totalVal / Math.pow(bOut, xCount)) >= bOut) {
	 	    	xCount ++;
	 	    }	    
	 	    
	 	    int charOutVal = 0;
	 	    //convert from base10 to baseOut
	     	
	 	    for (int count = (int) xCount; count >= 0; count--) {
	 	    	//System.out.println(count);
	 	    	charOutVal = (int) (totalVal / Math.pow(bOut, count));
	 	    		    	
	 	    	totalVal = (long) Math.round(totalVal - charOutVal * Math.pow(bOut, count)); 	    	
	 	    	
	 	    	
	 	    	if ((charOutVal >= 0) && (charOutVal <= 9)) {
	 	    		charOutVal += 48;
	 	    	} else if (charOutVal >= 10 && charOutVal <= 35) {
	 	    		charOutVal += 55;
	 	    	} else if (charOutVal >= 36 && charOutVal <= 61) {
	 	    		charOutVal += 61;
	 	    	}

	 	    	//System.out.println(charOutVal);
	 	    	out += Character.toString((char)charOutVal);
	 	    	
	 	    }
	 	}
	}
	
	
	public String getOutput() {
		return out;
	}
	
	
	private int bIn, bOut = 0;
	private String num, out = "";
	private long totalVal = 0;
	
}
